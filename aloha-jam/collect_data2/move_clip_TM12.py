import rospy
from tm_msgs.srv import SetIO, SetIORequest, SetIOResponse

def set_io_demo():
    rospy.init_node('demo_set_io')
    rospy.wait_for_service('tm_driver/set_io')
    try:
        set_io_service = rospy.ServiceProxy('tm_driver/set_io', SetIO)
        request = SetIORequest()
        request.module = SetIORequest.MODULE_CONTROLBOX
        request.type = SetIORequest.TYPE_DIGITAL_OUT
        request.pin = 0
        request.state = 0

        response = set_io_service(request)
        if response.ok:
            rospy.loginfo("SetIO to robot successful")
        else:
            rospy.logwarn("SetIO to robot, but response not yet ok")
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s" % e)

if __name__ == "__main__":
    set_io_demo()
