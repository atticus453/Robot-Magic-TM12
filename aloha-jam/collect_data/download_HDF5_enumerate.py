import os

# 文件ID列表，可以分批添加多个文件ID
file_ids = [
    '1pnGIOd-E4-rhz2P3VxpknMKRZCoKt6eI',  # Replace with your file ID
    '1GKReZHrXU73NMiC5zKCq_UtqPVtYq8eo',  # Replace with your file ID
    # Add more file IDs as needed
]

# 目标文件夹
destination = '~/train_data'
destination = os.path.expanduser(destination)

# 如果目标文件夹不存在，则创建它
if not os.path.exists(destination):
    os.makedirs(destination)

# 分批下载文件，并按指定格式命名
for idx, file_id in enumerate(file_ids):
    output_path = os.path.join(destination, f'episode_{idx+48}.hdf5')
    os.system(f'gdown https://drive.google.com/uc?id={file_id} -O {output_path} --remaining-ok')

print("下载完成!")
