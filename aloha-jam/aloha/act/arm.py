Atticus
atticus453
線上

許凱棋 — 2024/07/11 10:31
hello
import h5py
import numpy as np
文件路徑
file_path = 'C:/act-main/0708/episode_0.hdf5'

def read_and_print_group(group, group_name=""):
    """
    遍歷並讀取群組中的所有數據集，並打印其內容。
    """
    for key, item in group.items():
        full_key = f"{group_name}/{key}" if group_name else key
        if isinstance(item, h5py.Dataset):
            data = item[:]
            print(f'Length of {full_key}: {len(data)}')
            print(f'Data from {full_key}:')
            print(data)
        elif isinstance(item, h5py.Group):
            read_and_print_group(item, full_key)

with h5py.File(file_path, 'r') as file:
    read_and_print_group(file)
Atticus — 2024/07/11 10:32
hello world
`
許凱棋 — 2024/07/11 10:32
import h5py
import numpy as np
# 文件路徑
file_path = 'C:/act-main/0708/episode_0.hdf5'

def read_and_print_group(group, group_name=""):
    """
    遍歷並讀取群組中的所有數據集，並打印其內容。
    """
    for key, item in group.items():
        full_key = f"{group_name}/{key}" if group_name else key
        if isinstance(item, h5py.Dataset):
            data = item[:]
            print(f'Length of {full_key}: {len(data)}')
            print(f'Data from {full_key}:')
            print(data)
        elif isinstance(item, h5py.Group):
            read_and_print_group(item, full_key)

with h5py.File(file_path, 'r') as file:
    read_and_print_group(file)
許凱棋 — 2024/07/12 15:43
附件檔案類型：acrobat
Expression Editor and Listen Node_1.76_Rev1.00_TW.pdf
4.19 MB
許凱棋 — 2024/07/22 11:05
https://github.com/tonyzhaozh/aloha/tree/main
GitHub
GitHub - tonyzhaozh/aloha
Contribute to tonyzhaozh/aloha development by creating an account on GitHub.
GitHub - tonyzhaozh/aloha
許凱棋 — 2024/07/23 09:39
https://blog.csdn.net/joyopirate/article/details/129424607
在ROS2中，通过MoveIt2控制Gazebo中的自定义机械手-CSDN博客
文章浏览阅读1.1w次，点赞53次，收藏217次。目前的空余时间主要都在研究ROS2，最终目的是控制自己用舵机组装的机械手。由于种种原因，先控制Gazebo的自定义机械手先。先看看目前的成果左侧是rviz2中的moveit组件的机械手，右侧是gazebo中的机械手。在moveit中进行路径规划并执行后，右侧gazebo中的机械手也就执行相应的动作。据说win10下也可以装ROS2，但是十分折腾，还是在Ubuntu下安装方便一些，Ubuntu22.04才有humble版本的ros2，Ubuntu20.04没有humble。按照鱼香ros的教程，在命令行_moveit2
許凱棋 — 2024/08/02 12:44
https://github.com/TechmanRobotInc/tmr_ros1.git
GitHub
GitHub - TechmanRobotInc/tmr_ros1: TM Robots supporting ROS1 driver...
TM Robots supporting ROS1 drivers and some extended external applications. (experimental) (not support the new TM S-Series) - TechmanRobotInc/tmr_ros1
GitHub - TechmanRobotInc/tmr_ros1: TM Robots supporting ROS1 driver...
許凱棋 — 2024/08/06 12:19
附件檔案類型：document
TM12_ros_gazebo_simulation_short.pptx
601.34 KB
許凱棋 — 2024/08/14 14:28
附件檔案類型：acrobat
Software_TMvision_2.18_1.00_TW.pdf
10.83 MB
許凱棋 — 2024/08/14 14:55
austinwu1230@gmail.com
許凱棋 — 昨天 14:14
圖片
許凱棋 — 昨天 17:10
#!/usr/bin/env python

import os
import rospy
from tm_msgs.srv import SetPositions, SetPositionsRequest, SetIO, SetIORequest, SetIOResponse
from tm_msgs.msg import FeedbackState
展開
message.txt
5 KB
﻿
許凱棋
hsu_kai_chi
 
#!/usr/bin/env python

import os
import rospy
from tm_msgs.srv import SetPositions, SetPositionsRequest, SetIO, SetIORequest, SetIOResponse
from tm_msgs.msg import FeedbackState
from sensor_msgs.msg import Image
import sys
import cv2
from cv_bridge import CvBridge, CvBridgeError
import message_filters

pre_position = []
now_position = []

def callback(feedback_msg, image_msg):
    # 獲取時間戳
    timestamp = feedback_msg.header.stamp.to_sec()

    # 生成 txt 檔案名稱
    txt_filename = "status/{}.txt".format(timestamp)
    
    # 寫入 joint pos 和 cb_digital_output 到 txt 文件
    with open(txt_filename, "w") as file:
        file.write("{}, {}, {}, {}, {}, {}, {}\n".format(
            feedback_msg.joint_pos[0],
            feedback_msg.joint_pos[1],
            feedback_msg.joint_pos[2],
            feedback_msg.joint_pos[3],
            feedback_msg.joint_pos[4],
            feedback_msg.joint_pos[5],
            feedback_msg.cb_digital_output[0]
        ))

    # 生成 jpg 檔案名稱
    jpg_filename = "status/{}.jpg".format(timestamp)

    # 将图像消息转换为OpenCV格式并保存为jpg
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(image_msg, "bgr8")
    cv2.imwrite(jpg_filename, cv_image)
    rospy.loginfo("Saved {} and {}".format(txt_filename, jpg_filename))


def set_clip(clip):
    rospy.wait_for_service('tm_driver/set_io')
    try:
        set_io_service = rospy.ServiceProxy('tm_driver/set_io', SetIO)
        request = SetIORequest()
        request.module = SetIORequest.MODULE_CONTROLBOX
        request.type = SetIORequest.TYPE_DIGITAL_OUT
        request.pin = 0

        if clip == 1: request.state = SetIORequest.STATE_ON
        else:
            request.state = SetIORequest.STATE_OFF
        response = set_io_service(request)

    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s" % e)

def image_callback(msg):
    timestamp = msg.header.stamp
    bridge = CvBridge()
    try:
        # 將 ROS Image 訊息轉換為 OpenCV 圖像
        cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        # 確保目標資料夾存在
        folder_path = 'image'
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        # 保存 OpenCV 圖像為 JPEG 文件
        filename = f"{timestamp.secs}_{timestamp.nsecs}.jpg"
        file_path = os.path.join(folder_path, filename)
        cv2.imwrite(file_path, cv_image)
        
    except CvBridgeError as e:
        rospy.logerr(f"Failed to convert image: {e}")

def move_arm(joint_positions):
    rospy.init_node('move_real_tm12_arm_from_file', anonymous=True)
    rospy.wait_for_service('tm_driver/set_positions')
    last_clip = 0;
    try:
        set_positions = rospy.ServiceProxy('tm_driver/set_positions', SetPositions)
        now_pos = joint_positions[0]
        for positions in joint_positions:
            feedback_sub = message_filters.Subscriber("feedback_states", FeedbackState)
            image_sub = message_filters.Subscriber("/camera/image", Image)
    # 同步這兩個話題
            ts = message_filters.ApproximateTimeSynchronizer([feedback_sub, image_sub], queue_size=10, slop=0.1)
            ts.registerCallback(callback)

            req = SetPositionsRequest()
            req.motion_type = SetPositionsRequest.PTP_J
            req.positions = [positions[0],positions[1],positions[2],positions[3],positions[4],positions[5]]
            req.velocity = 1.0  # rad/s
            req.acc_time = 0.2
            req.blend_percentage = 10
            req.fine_goal = True
            response = set_positions(req)
            set_clip(positions[6])
            if(last_clip != positions[6]):
               last_clip = positions[6]
               rospy.sleep(5.0)
            else:
               rospy.sleep(2.0)
    except rospy.ServiceException as e:
        rospy.logerr(f"Service call failed: {e}")

def read_joint_positions(file_path):
    joint_positions = []
    with open(file_path, 'r') as file:
        for line in file:
            positions = [float(x) for x in line.strip().split(',')]
            joint_positions.append(positions)
    return joint_positions

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: TM12_pos_from_file.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    
    try:
        joint_positions = read_joint_positions(file_path)
        move_arm(joint_positions)
    except rospy.ROSInterruptException:
        pass