#!/usr/bin/env python


import rospy
from tm_msgs.srv import SetPositions, SetPositionsRequest, SetIO, SetIORequest, SetIOResponse
from tm_msgs.msg import FeedbackState
from sensor_msgs.msg import Image
import sys
import cv2
from cv_bridge import CvBridge, CvBridgeError
import message_filters
import h5py


def read_joint_positions(action):
    joint_positions = []
    positions = []
# 逐一轉換展平後的元素
    i = 0
    while(i < 100):
        positions = [action[i][0],action[i][1],action[i][2],action[i][3],action[i][4],action[i][5],action[i][6]]
        joint_positions.append(positions)
        i+=1
    return joint_positions

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

def move_arm(joint_positions):
    rospy.init_node('move_real_tm12_arm_from_file', anonymous=True)
    rospy.wait_for_service('tm_driver/set_positions')
    last_clip = 0.0

    try:
        set_positions = rospy.ServiceProxy('tm_driver/set_positions', SetPositions)
        now_pos = joint_positions[0]
        for positions in joint_positions:
            print([positions[0],positions[1],positions[2],positions[3],positions[4],positions[5]])
            req = SetPositionsRequest()
            req.motion_type = SetPositionsRequest.PTP_J
            req.positions = [positions[0],positions[1],positions[2],positions[3],positions[4],positions[5]]
            req.velocity = 1.0  # rad/s
            req.acc_time = 0.2
            req.blend_percentage = 10
            req.fine_goal = False
            response = set_positions(req)
            set_clip(positions[6])
            if(last_clip != positions[6]):
               last_clip = positions[6]
               rospy.sleep(2.0)

    except rospy.ServiceException as e:
        rospy.logerr(f"Service call failed: {e}")

def read_hdf5_action(file_path):
    with h5py.File(file_path, 'r') as root:
        action_data = root['/action'][...] 
        return action_data

def read_hdf5_qpos(file_path):
    with h5py.File(file_path, 'r') as root:
        qpos_data = root['/observations/qpos'][...]
        return qpos_data

if __name__ == '__main__':
    
    file_path = ('status/test_1.hdf5')

    try:
        qpos = read_hdf5_qpos(file_path)
        qpos_joint_positions = read_joint_positions(qpos)
        move_arm(qpos_joint_positions)
        action = read_hdf5_action(file_path)
        act_joint_positions = read_joint_positions(action)
        move_arm(act_joint_positions)
        file_name = 'example.txt'

        with open(file_name, 'w') as file:
            for position in act_joint_positions:
                line = ' '.join(map(str, position))
                file.write(line + '\n')
            for q_position in qpos_joint_positions:
                line = ' '.join(map(str, q_position))
                file.write(line + '\n')

    except rospy.ROSInterruptException:
        pass