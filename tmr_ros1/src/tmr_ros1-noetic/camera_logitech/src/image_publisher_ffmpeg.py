#!/usr/bin/env python3

import rospy
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import subprocess

def main():
    rospy.init_node('image_publisher', anonymous=True)
    image_pub = rospy.Publisher('/camera/image_raw2', Image, queue_size=10)
    bridge = CvBridge()

    # 使用FFmpeg通过管道接收影像流
    ffmpeg_command = [
        'ffmpeg',
        '-protocol_whitelist', 'file,udp,rtp',  # 允许的协议
        '-i', 'udp://0.0.0.0:5000',        # 从UDP端口5000接收影像流
        '-f', 'image2pipe',                     # 输出格式为图像管道
        '-pix_fmt', 'bgr24',                    # 像素格式设置为BGR24
        '-vcodec', 'rawvideo',                  # 使用原始视频编码
        '-'
    ]

    ffmpeg_process = subprocess.Popen(ffmpeg_command, stdout=subprocess.PIPE, bufsize=10**8)

    rate = rospy.Rate(30)  # 30Hz
    while not rospy.is_shutdown():
        raw_image = ffmpeg_process.stdout.read(640*480*3)  # 假设解析度为640x480
        if len(raw_image) != 640*480*3:
            rospy.logerr("Failed to capture image")
            continue

        # 将原始数据转换为NumPy数组
        image = np.frombuffer(raw_image, np.uint8).reshape((480, 640, 3))

        # 将图像转换为ROS Image消息
        image_msg = bridge.cv2_to_imgmsg(image, "bgr8")
        image_pub.publish(image_msg)

        rate.sleep()

    ffmpeg_process.terminate()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
