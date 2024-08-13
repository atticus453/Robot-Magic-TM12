#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64MultiArray

def move_arm_once(joint_positions):
    pub = rospy.Publisher('/joint_group_position_controller/command', Float64MultiArray, queue_size=10)
    rospy.init_node('move_arm_once', anonymous=True)
    
    # wait for connection
    rospy.sleep(1)

    msg = Float64MultiArray()
    msg.data = joint_positions
    rospy.loginfo(f"Moving joints to positions: {joint_positions}")
    pub.publish(msg)

if __name__ == '__main__':
    try:
        # set joint positions
        joint_positions = [0.0, 0.5, 0.0, 0.0, 0.0, 0.0]
        move_arm_once(joint_positions)
    except rospy.ROSInterruptException:
        pass

