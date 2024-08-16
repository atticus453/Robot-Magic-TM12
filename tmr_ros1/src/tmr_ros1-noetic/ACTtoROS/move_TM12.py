#!/usr/bin/env python

import rospy
from tm_msgs.srv import SetPositions, SetPositionsRequest
import sys

def move_arm(joint_positions):
    rospy.init_node('move_real_tm12_arm_from_file', anonymous=True)
    rospy.wait_for_service('tm_driver/set_positions')

    try:
        set_positions = rospy.ServiceProxy('tm_driver/set_positions', SetPositions)

        for positions in joint_positions:
            req = SetPositionsRequest()
            req.motion_type = SetPositionsRequest.PTP_J
            req.positions = positions
            req.velocity = 0.4  # rad/s
            req.acc_time = 0.2
            req.blend_percentage = 10
            req.fine_goal = False

            rospy.loginfo(f"Moving joints to positions: {positions}")
            response = set_positions(req)

            if response.ok:
                rospy.loginfo("Movement successful")
            else:
                rospy.logwarn("Movement not confirmed by robot")

            rospy.sleep(0.1)  # Sleep between movements

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
