import h5py
import os

def add_sim_attribute(hdf5_file):
    with h5py.File(hdf5_file, 'a') as f:
        # Check if the attribute exists
        if 'sim' not in f.attrs:
            # Add the 'sim' attribute (assuming it's a boolean, set it according to your needs)
            f.attrs['sim'] = True
            print(f"Added 'sim' attribute to {hdf5_file}")
        else:
            print(f"'sim' attribute already exists in {hdf5_file}")

def process_all_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".hdf5"):
            add_sim_attribute(os.path.join(directory, filename))

if __name__ == "__main__":
    hdf5_directory = '/home/jiayulin/train_data2/aloha_mobile_dummy/'
    process_all_files(hdf5_directory)
