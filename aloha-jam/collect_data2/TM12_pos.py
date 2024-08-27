#!/usr/bin/env python

import rospy
from tm_msgs.msg import FeedbackState

def TMmsgCallback(msg):
    if len(msg.joint_pos) == 6:
        rospy.loginfo("FeedbackState: joint pos = ({}, {}, {}, {}, {}, {})".format(
            msg.joint_pos[0],
            msg.joint_pos[1],
            msg.joint_pos[2],
            msg.joint_pos[3],
            msg.joint_pos[4],
            msg.joint_pos[5]
        ))
    else:
        rospy.logerr("Error FeedbackState callback")

def main():
    rospy.init_node('FeedbackState', anonymous=True)
    rospy.Subscriber("feedback_states", FeedbackState, TMmsgCallback)
    rospy.spin()
if __name__ == '__main__':
    main()
