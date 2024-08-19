#!/home/jiayulin/miniconda3/envs/ros_env_tm12/bin/python3
# -*- coding: utf-8 -*-
# generated from catkin/cmake/template/script.py.in
# creates a relay to a python script source file, acting as that file.
# The purpose is that of a symlink
python_script = '/home/jiayulin/robot_magic_tm12/tmr_ros1/src/tmr_ros1-noetic/camera_logitech/src/image_publisher_ffmpeg.py'
with open(python_script, 'r') as fh:
    context = {
        '__builtins__': __builtins__,
        '__doc__': None,
        '__file__': python_script,
        '__name__': __name__,
        '__package__': None,
    }
    exec(compile(fh.read(), python_script, 'exec'), context)
