import cv2
import socket
import numpy as np
import struct
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

# 设置 TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('10.72.221.29', 9999))
sock.listen(1)

conn, addr = sock.accept()

data = b""
payload_size = struct.calcsize(">L")

# 初始化 ROS 节点
rospy.init_node('image_publisher_node', anonymous=True)
image_pub = rospy.Publisher('/camera/image', Image, queue_size=10)
bridge = CvBridge()

while not rospy.is_shutdown():
    # 接收图像大小
    while len(data) < payload_size:
        data += conn.recv(4096)
    
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack(">L", packed_msg_size)[0]

    # 接收图像数据
    while len(data) < msg_size:
        data += conn.recv(4096)

    frame_data = data[:msg_size]
    data = data[msg_size:]

    # 将字节数据转换回图像
    np_data = np.frombuffer(frame_data, dtype=np.uint8)
    frame = cv2.imdecode(np_data, cv2.IMREAD_COLOR)

    # 显示接收到的影像
    if frame is not None:
        #cv2.imshow('Received Feed', frame)
        # 将 OpenCV 图像转换为 ROS 图像消息并发布
        ros_image = bridge.cv2_to_imgmsg(frame, encoding="bgr8")
        ros_image.header.stamp = rospy.Time.now()
        image_pub.publish(ros_image)

    # 如果按下 'q' 键，则退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 关闭连接
conn.close()
cv2.destroyAllWindows()
