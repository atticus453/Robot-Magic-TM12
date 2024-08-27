import cv2
import socket
import numpy as np
import struct
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

# 设置 TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('10.72.221.29', 9998))
sock.listen(1)

conn, addr = sock.accept()

data = b""
payload_size = struct.calcsize(">L")

# 初始化 ROS 节点
rospy.init_node('depthimage_publisher_node', anonymous=True)
rgb_image_pub = rospy.Publisher('/depth_camera/rgb_image', Image, queue_size=10)
depth_image_pub = rospy.Publisher('/depth_camera/depth_image', Image, queue_size=10)
bridge = CvBridge()

while not rospy.is_shutdown():
    # 接收RGB图像大小
    while len(data) < payload_size:
        data += conn.recv(4096)
    
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    rgb_msg_size = struct.unpack(">L", packed_msg_size)[0]

    # 接收RGB图像数据
    while len(data) < rgb_msg_size:
        data += conn.recv(4096)

    rgb_frame_data = data[:rgb_msg_size]
    data = data[rgb_msg_size:]

    # 将字节数据转换回RGB图像
    rgb_np_data = np.frombuffer(rgb_frame_data, dtype=np.uint8)
    rgb_frame = cv2.imdecode(rgb_np_data, cv2.IMREAD_COLOR)

    # 接收深度图像大小
    while len(data) < payload_size:
        data += conn.recv(4096)
    
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    depth_msg_size = struct.unpack(">L", packed_msg_size)[0]

    # 接收深度图像数据
    while len(data) < depth_msg_size:
        data += conn.recv(4096)

    depth_frame_data = data[:depth_msg_size]
    data = data[depth_msg_size:]

    # 将字节数据转换回深度图像
    depth_np_data = np.frombuffer(depth_frame_data, dtype=np.uint8)
    depth_frame = cv2.imdecode(depth_np_data, cv2.IMREAD_COLOR)  # 如果深度图像是单通道，你可能需要调整这里

    # 发布RGB图像
    if rgb_frame is not None:
        ros_rgb_image = bridge.cv2_to_imgmsg(rgb_frame, encoding="bgr8")
        ros_rgb_image.header.stamp = rospy.Time.now()
        rgb_image_pub.publish(ros_rgb_image)

    # 发布深度图像
    if depth_frame is not None:
        ros_depth_image = bridge.cv2_to_imgmsg(depth_frame, encoding="bgr8")
        ros_depth_image.header.stamp = rospy.Time.now()
        depth_image_pub.publish(ros_depth_image)

    # 如果按下 'q' 键，则退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 关闭连接
conn.close()
cv2.destroyAllWindows()
