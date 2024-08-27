import os
import subprocess
import gdown

def download_folder_from_drive(drive_folder_id, destination):
    # Check if gdown is installed
    try:
        import gdown
    except ImportError:
        raise ImportError("Please install gdown by running 'pip install gdown'.")

    # Expand the user's home directory in the destination path
    destination = os.path.expanduser(destination)
    
    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination):
        os.makedirs(destination)
    
    # Build the gdown command to download the entire folder
    command = f"gdown --folder https://drive.google.com/drive/folders/{drive_folder_id} -O {destination} --remaining-ok"
    
    try:
        # Execute the command
        subprocess.run(command, shell=True, check=True)
        print(f"Folder downloaded successfully to {destination}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # The Google Drive folder ID (from the URL)
    drive_folder_id = "1aRyoOhQwxhyt1J8XgEig4s6kzaw__LXj"
    
    # The destination directory where the folder will be downloaded
    destination = "~/train_data"
    
    # Download the folder
    download_folder_from_drive(drive_folder_id, destination)
