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

num_elements = 200
long_position_list = []
long_image_high_list = []
long_image_left_list = []
long_depth_image_high_list = []
long_depth_image_left_list = []
long_velocity_list = []
long_effort_list = []

def callback(feedback_msg, image_msg_high,image_msg_left,depth_image_msg_high,depth_image_msg_left):
    # 獲取時間戳
    timestamp = feedback_msg.header.stamp.to_sec()

    long_position_list.append([feedback_msg.joint_pos[0],
        feedback_msg.joint_pos[1],
        feedback_msg.joint_pos[2],
        feedback_msg.joint_pos[3],
        feedback_msg.joint_pos[4],
        feedback_msg.joint_pos[5],
        feedback_msg.cb_digital_output[0],0,0,0,0,0,0,0])
    
    long_velocity_list.append([feedback_msg.joint_vel[0],
        feedback_msg.joint_vel[1],
        feedback_msg.joint_vel[2],
        feedback_msg.joint_vel[3],
        feedback_msg.joint_vel[4],
        feedback_msg.joint_vel[5],
        feedback_msg.cb_digital_output[0],0,0,0,0,0,0,0])
    
    long_effort_list.append([feedback_msg.joint_tor[0],
        feedback_msg.joint_tor[1],
        feedback_msg.joint_tor[2],
        feedback_msg.joint_tor[3],
        feedback_msg.joint_tor[4],
        feedback_msg.joint_tor[5],
        feedback_msg.cb_digital_output[0],0,0,0,0,0,0,0])
    
    bridge = CvBridge()

    cv_high_image = bridge.imgmsg_to_cv2(image_msg_high, 'passthrough')
    long_image_high_list.append(cv_high_image)

    cv_left_image = bridge.imgmsg_to_cv2(image_msg_left, 'passthrough')
    long_image_left_list.append(cv_left_image)

    cv_depth_high_image = bridge.imgmsg_to_cv2(depth_image_msg_high, 'passthrough')
    long_depth_image_high_list.append(cv_depth_high_image)


    cv_depth_left_image = bridge.imgmsg_to_cv2(depth_image_msg_left, 'passthrough')
    long_depth_image_left_list.append(cv_depth_left_image)


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
    last_clip = 0
    
    try:
        set_positions = rospy.ServiceProxy('tm_driver/set_positions', SetPositions)
        for positions in joint_positions:
            
            feedback_sub = message_filters.Subscriber("feedback_states", FeedbackState)
            image_sub_high = message_filters.Subscriber("/depth_camera_right/rgb_image", Image)
            image_sub_left = message_filters.Subscriber("/depth_camera_gripper/rgb_image", Image)
            depth_image_sub_high = message_filters.Subscriber("/depth_camera_right/depth_image", Image)
            depth_image_sub_left = message_filters.Subscriber("/depth_camera_gripper/depth_image", Image)
            
            #image_sub_right = message_filters.Subscriber("/camera/image", Image)
            #depth_image_sub_right = message_filters.Subscriber("/camera/image", Image)
            rospy.sleep(0.5)

            ts = message_filters.ApproximateTimeSynchronizer([feedback_sub, image_sub_high,image_sub_left, depth_image_sub_high,depth_image_sub_left], queue_size=10, slop=0.1)
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
               rospy.sleep(4.0)

            else : rospy.sleep(1.0)

    except rospy.ServiceException as e:
        rospy.logerr(f"Service call failed: {e}")

def read_joint_positions(file_path):
    joint_positions = []
    with open(file_path, 'r') as file:
        for line in file:
            positions = [float(x) for x in line.strip().split(',')]
            joint_positions.append(positions)
    return joint_positions

def create_hdf5():
     step = (len(long_position_list)-2) // (num_elements-2)

     position_list = []
     velocity_list = []
     effort_list = []
     image_high_list = []
     image_left_list = []
     depth_image_high_list = []
     depth_image_left_list = []

     position_list.append(long_position_list[0])
     velocity_list.append(long_velocity_list[0])
     effort_list.append(long_effort_list[0]) 
     image_high_list.append(long_image_high_list[0])
     image_left_list.append(long_image_left_list[0])
     depth_image_high_list.append(long_depth_image_high_list[0])  
     depth_image_left_list.append(long_depth_image_left_list[0])

     for i in range(num_elements-2):
        position_list.append(long_position_list[int(i * step)])
        velocity_list.append(long_velocity_list[int(i * step)])
        effort_list.append(long_effort_list[int(i * step)]) 
        image_high_list.append(long_image_high_list[int(i * step)])
        image_left_list.append(long_image_left_list[int(i * step)])
        depth_image_high_list.append(long_depth_image_high_list[int(i * step)])  
        depth_image_left_list.append(long_depth_image_left_list[int(i * step)])

     position_list.append(long_position_list[len(long_position_list)-1])
     velocity_list.append(long_velocity_list[len(long_velocity_list)-1])
     effort_list.append(long_effort_list[len(long_effort_list)-1]) 
     image_high_list.append(long_image_high_list[len(long_image_high_list)-1])
     image_left_list.append(long_image_left_list[len(long_image_left_list)-1])
     depth_image_high_list.append(long_depth_image_high_list[len(long_depth_image_high_list)-1])  
     depth_image_left_list.append(long_depth_image_left_list[len(long_depth_image_left_list)-1])

     with h5py.File('status/test_1' + '.hdf5', 'w', rdcc_nbytes=1024**2*2) as root:
        obs = root.create_group('observations')
        img = obs.create_group('images')
        dep_img = obs.create_group('images_depth')

        _ = dep_img.create_dataset('cam_high', (len(image_high_list)//2, 480, 640), dtype='uint16',
                                             chunks=(1, 480, 640))
        _ = dep_img.create_dataset('cam_left', (len(image_high_list)//2, 480, 640), dtype='uint16',
                                             chunks=(1, 480, 640))
        _ = dep_img.create_dataset('cam_right', (len(image_high_list)//2, 480, 640), dtype='uint16',
                                             chunks=(1, 480, 640))

        _ = img.create_dataset('cam_high', (len(image_high_list)//2, 480, 640, 3), dtype='uint8',
                                         chunks=(1, 480, 640, 3))
        _ = img.create_dataset('cam_left', (len(image_high_list)//2, 480, 640, 3), dtype='uint8',
                                         chunks=(1, 480, 640, 3))
        _ = img.create_dataset('cam_right', (len(image_high_list)//2, 480, 640, 3), dtype='uint8',
                                         chunks=(1, 480, 640, 3))

        _ = obs.create_dataset('qpos', (len(position_list)//2, 14))
        _ = obs.create_dataset('qvel', (len(velocity_list)//2, 14))
        _ = obs.create_dataset('effort', (len(effort_list)//2, 14))
        _ = root.create_dataset('action', (len(position_list)//2, 14))

        root['/action'][...] = position_list[len(position_list)//2:]
        root['/observations/qpos'][...] = position_list[:len(position_list)//2]
        root['/observations/qvel'][...] = velocity_list[:len(velocity_list)//2]
        root['/observations/effort'][...] = effort_list[:len(effort_list)//2]
        root['/observations/images/cam_high'][...] = image_high_list[:len(image_high_list)//2]
        root['/observations/images/cam_left'][...] = image_left_list[:len(image_left_list)//2]
        root['/observations/images_depth/cam_high'][...] = depth_image_high_list[:len(depth_image_high_list)//2]
        root['/observations/images_depth/cam_left'][...] = depth_image_left_list[:len(depth_image_left_list)//2]

        root['/observations/images/cam_right'][...] = image_high_list[:len(image_high_list)//2]
        root['/observations/images_depth/cam_right'][...] = depth_image_high_list[:len(image_high_list)//2]

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: TM12_pos_from_file.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    
    try:
        joint_positions = read_joint_positions(file_path)
        move_arm(joint_positions)
        create_hdf5()
    except rospy.ROSInterruptException:
        pass
