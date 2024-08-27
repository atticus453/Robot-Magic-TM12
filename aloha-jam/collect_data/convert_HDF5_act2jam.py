import h5py
import numpy as np

def convert_hdf5(source_path, target_path):
    with h5py.File(source_path, 'r') as source_file, h5py.File(target_path, 'w') as target_file:
        # Copy the "action" dataset
        if "action" in source_file:
            source_file.copy("action", target_file)
        
        # Create the "base_action" dataset and fill with zeros if not present
        if "base_action" not in source_file:
            target_file.create_dataset("base_action", data=np.zeros((0,)))

        # Copy "observations" group
        observations_group = target_file.create_group("observations")

        # Copy and transform "images" datasets
        if "images" in source_file["observations"]:
            images_group = observations_group.create_group("images")
            for cam in ["cam_high", "cam_left_wrist", "cam_right_wrist"]:
                if "top" in source_file["observations/images"]:
                    images_group.create_dataset(cam, data=source_file["observations/images"]["top"][:])
                else:
                    images_group.create_dataset(cam, data=np.zeros_like(source_file["observations/images"]["top"][:]))

        # Create and fill "images_depth" group with zeros if not present
        images_depth_group = observations_group.create_group("images_depth")
        for cam in ["cam_high", "cam_left_wrist", "cam_right_wrist"]:
            images_depth_group.create_dataset(cam, data=np.zeros_like(source_file["observations/images"]["top"][:]))

        # Copy "qpos" and "qvel" datasets
        for dataset_name in ["qpos", "qvel"]:
            if dataset_name in source_file["observations"]:
                observations_group.create_dataset(dataset_name, data=source_file["observations"][dataset_name][:])
            else:
                observations_group.create_dataset(dataset_name, data=np.zeros((0,)))

        # Create and fill "effort" dataset with zeros if not present
        if "effort" not in source_file["observations"]:
            observations_group.create_dataset("effort", data=np.zeros_like(source_file["observations"]["qpos"][:]))
        print("successfully copied one hdf5")

if __name__ == "__main__":
    # for i in range(50):
    # convert_hdf5(f'/home/jiayulin/train_data/episode_{i}.hdf5', f'/home/jiayulin/train_data_converted/episode_{i}.hdf5')
    convert_hdf5(f'/home/jiayulin/train_data/episode_49.hdf5', f'/home/jiayulin/train_data_converted/episode_49.hdf5')
