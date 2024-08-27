# JAM : Imitation Learning with TM12 Robotic Arms



### Repo Structure
- ``tmr2_ros1`` TM12 ROS1 Driver
- ``aloha-jam`` Integrate **TM12 ROS control** with **ACT**


### Installation
    
    $ git clone https://github.com/atticus453/robot_magic_tm12.git
    
    
### Camera Setup

    (On server,the computer harboring ACT)
    $ cd ~/Robot-Magic-TM12/camera_ws/src/camera_pkg
    $ conda env create -f environment_receive.yml
    $ conda activate camera_receive_env
    $ cd ~/Robot-Magic-TM12/camera_ws/
    $ catkin_make
    $ source devel/setup.sh
    $ rosrun camera_pkg receive.py
    $ rosrun camera_pkg receive_depth.py


    (On Win10,the computer that connect with cameras)
    $ cd ~/Robot-Magic-TM12/camera/src/camera_send
    $ conda env create -f environment_send.yml
    $ conda activate camera_send_env
    $ python camera.py
    $ python depthcamera.py
    
### Example Usages #1: Launch tm12 in Gazebo with Camera
    
    Note: this usage is under maintenance
    $ conda activate ros_env_tm12
    $ cd ~/Robot-Magic-TM12/hardware_setup/tm2_ros1_ws
    $ source devel/setup.sh
    $ roslaunch tm_gazebo tm12_gazebo.launch
    
    Note: control the camera robot
    $ rosrun teleop_twist_keyboard teleop_twist_keyboard.py 
    
    Note: view the image from Camera
    $ rqt_image_view
    
### Example Usages #2: Generate fake HDF5 
    
    Note: Typically, <your virtual env name> = env_train_inference
    $ conda activate env_train_inference
    $ cd ~/Robot-Magic-TM12/aloha-jam/
    
    Note: fake HDF5 files are under "~/data/aloha_mobile_dummy"
    $ python collect_data/fake_HDF5_collect.py 

### Example Usages #3: Train ACT Model
    
    Note: Typically, <your virtual env name> = env_train_inference
    
    $ cd ~/Robot-Magic-TM12/cobot_magic-main
    $ conda env create -f environment_train_infer.yml
    $ conda activate env_train_inference
    $ cd ~/Robot-Magic-TM12/aloha-jam/aloha
    
    Note: Make sure you have HDF5 files for training usage
    $  python act/train.py --dataset_dir ~/data --pretrain_ckpt ~/data/pretrained --ckpt_dir ~/train_dir/ --num_episodes 10 --batch_size 5  --num_epochs 2
    
    
    
    
    
### Example Usages #4: Inferencing in Real TM12
    
    Note: remember to activate Camera
    
    Note: setup tm12's driver 
    $ cd ~/Robot-Magic-TM12/hardware_setup/tm2_ros1_ws
    $ conda env create -f environment_tm12.yml 
    $ conda activate ros_env_tm12_build
    $ export LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH
    $ catkin_make
    $ source devel/setup.sh 
    
    Note: create a virtual env
    $ cd ~/Robot-Magic-TM12/cobot_magic-main
    $ conda env create -f environment_train_infer.yml
    $ conda activate env_train_inference
    $ export LD_LIBRARY_PATH=$(conda info --base)/envs/env_train_inference/lib:$LD_LIBRARY_PATH
    


    
    Note: start inference 
    $ cd ~/Robot-Magic-TM12/aloha-jam/aloha
    $ python act/inference.py --ckpt_dir ~/ckpt_new/ 
    
    
    

### Example Usages #4: ...
    
    to be continued
    
