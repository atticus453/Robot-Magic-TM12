#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64MultiArray
import time

def move_arm(joint_positions):
    pub = rospy.Publisher('/joint_group_position_controller/command', Float64MultiArray, queue_size=10)
    rospy.init_node('move_arm_from_file', anonymous=True)
    
    rospy.sleep(1)

    for positions in joint_positions:
        msg = Float64MultiArray()
        msg.data = positions
        rospy.loginfo(f"Moving joints to positions: {positions}")
        pub.publish(msg)
        rospy.sleep(1) 

def read_joint_positions(file_path):
    joint_positions = []
    with open(file_path, 'r') as file:
        for line in file:
            positions = [float(x) for x in line.strip().split(',')]
            joint_positions.append(positions)
    return joint_positions

if __name__ == '__main__':
    try:
        file_path = 'joint_positions.txt'
        joint_positions = read_joint_positions(file_path)
        move_arm(joint_positions)
    except rospy.ROSInterruptException:
        pass
