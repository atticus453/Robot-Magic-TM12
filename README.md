# <topic TBD>: Imitation Learning with TM12 Robotic Arms



### Repo Structure
- ``tmr_ros1`` TM12 ROS1 Driver
- ``cobot_nagic-main`` Integrate **TM12 ROS control** with **ACT**


### Installation
    
    $ git clone https://github.com/atticus453/robot_magic_tm12.git
    
    (create a virtual env eith conda)
    $ conda env create -f environment.yml
    
    
### Example Usages #1: Launch tm12 in Gazebo with Camera
    
    $ conda activate ros_env_tm12
    $ cd ~/robot_magic_tm12/tmr_ros1
    $ source devel/setup.sh
    $ roslaunch tm_gazebo tm12_gazebo.launch
    
    (control the camera robot)
    $ rosrun teleop_twist_keyboard teleop_twist_keyboard.py 
    
    (view the image from Camera)
    $ rqt_image_view
    
### Example Usages #2: ...

    to be continued

### Training in Gazebo 

    to be continued    
    
### Inferencing in Gazebo 
    
    to be continued

### Inferencing in Real TM12 Robotic Arms
    
    to be continued
    
