#!/usr/bin/env python3

import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def gstreamer_pipeline():
    return ('udpsrc port=5000 caps="application/x-rtp,media=video,encoding-name=H264,payload=96" ! ' +
            'rtph264depay ! queue ! h264parse ! queue ! avdec_h264 ! queue ! videoconvert ! queue ! appsink drop=true max-buffers=1')

def main():
    rospy.init_node('image_publisher', anonymous=True)
    image_pub = rospy.Publisher('/camera/image_raw', Image, queue_size=10)
    bridge = CvBridge()

    # 使用GStreamer打開影像流
    cap = cv2.VideoCapture(gstreamer_pipeline(), cv2.CAP_GSTREAMER)

    if not cap.isOpened():
        rospy.logerr("Cannot open camera stream")
        return

    rate = rospy.Rate(10)  # 10Hz
    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if not ret:
            rospy.logerr("Failed to capture image")
            continue

        # 將捕獲的圖像轉換為ROS Image消息
        image_msg = bridge.cv2_to_imgmsg(frame, "bgr8")
        image_pub.publish(image_msg)

        rate.sleep()

    cap.release()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
