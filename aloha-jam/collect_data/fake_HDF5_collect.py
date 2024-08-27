import h5py
import numpy as np
import os

# 假設參數
num_episodes = 10
episode_length = 100  # 每個 episode 的步數
qpos_size = 14        # qpos 的大小
qvel_size = 14        # qvel 的大小
effort_size = 14      # effort 的大小
action_size = 14      # action 的大小
num_cameras = 3       # 使用的相機數量
image_shape = (480, 640, 3)  # 影像的大小
use_robot_base = True
use_depth_image = True

# 創建保存 HDF5 文件的資料夾
output_dir = os.path.expanduser('~/data/aloha_mobile_dummy')
os.makedirs(output_dir, exist_ok=True)

# 為每個 episode 創建單獨的 HDF5 文件
for episode_id in range(num_episodes):
    file_name = os.path.join(output_dir, f'episode_{episode_id}.hdf5')
    with h5py.File(file_name, 'w') as f:
        # 創建 /observations group
        obs_grp = f.create_group('observations')

        # 創建 qpos, qvel 和 effort 數據集
        qpos_data = np.random.rand(episode_length, qpos_size)
        qvel_data = np.random.rand(episode_length, qvel_size)
        effort_data = np.random.rand(episode_length, effort_size)
        obs_grp.create_dataset('qpos', data=qpos_data)
        obs_grp.create_dataset('qvel', data=qvel_data)
        obs_grp.create_dataset('effort', data=effort_data)
        
        # 創建 action 數據集
        action_data = np.random.rand(episode_length, action_size)
        f.create_dataset('action', data=action_data)
        
        # 如果使用 robot base，加入 base_action 數據
        if use_robot_base:
            base_action_data = np.random.rand(episode_length, 2)
            f.create_dataset('base_action', data=base_action_data)
        
        # 創建影像數據集
        images_grp = obs_grp.create_group('images')
        if use_depth_image:
            depth_images_grp = obs_grp.create_group('images_depth')
        
        for cam_id in range(num_cameras):
            if cam_id == 1:
                cam_name = 'cam_high'
            elif cam_id == 2:
                cam_name = 'cam_left_wrist'
            else:
                cam_name = 'cam_right_wrist'
            
            images = np.random.randint(0, 255, (episode_length,) + image_shape, dtype=np.uint8)
            images_grp.create_dataset(cam_name, data=images)
            
            if use_depth_image:
                depth_images = np.random.randint(0, 65535, (episode_length, image_shape[0], image_shape[1]), dtype=np.uint16)
                depth_images_grp.create_dataset(cam_name, data=depth_images)

        # 添加屬性
        f.attrs['sim'] = np.random.choice([True, False])
        f.attrs['compress'] = False

    print(f"Dummy HDF5 file '{file_name}' created successfully.")
