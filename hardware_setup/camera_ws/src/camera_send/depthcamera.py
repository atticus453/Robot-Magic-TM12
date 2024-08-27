import pyrealsense2 as rs
import numpy as np
import cv2
import socket
import struct

# 配置RealSense管道
pipeline = rs.pipeline()
config = rs.config()

# 啟用RGB和深度流
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# 开始串流
pipeline.start(config)

# 设置 TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('10.72.221.29', 9998)  # 替换为目标服务器的IP地址和端口
sock.connect(server_address)

try:
    while True:
        # 等待一个新的帧
        frames = pipeline.wait_for_frames()

        # 获取深度和RGB帧
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()

        if not depth_frame or not color_frame:
            continue

        # 转换深度帧为Numpy数组
        depth_image = np.asanyarray(depth_frame.get_data())
        # 转换RGB帧为Numpy数组
        color_image = np.asanyarray(color_frame.get_data())

        # 正规化深度影像以便显示
        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

        # 压缩RGB图像
        encoded_rgb, buffer_rgb = cv2.imencode('.jpg', color_image)
        message_rgb = buffer_rgb.tobytes()

        # 压缩深度图像
        encoded_depth, buffer_depth = cv2.imencode('.jpg', depth_colormap)
        message_depth = buffer_depth.tobytes()

        # 发送RGB图像大小和数据
        sock.sendall(struct.pack(">L", len(message_rgb)) + message_rgb)

        # 发送深度图像大小和数据
        sock.sendall(struct.pack(">L", len(message_depth)) + message_depth)

        # 显示图像
        cv2.imshow('RealSense RGB', color_image)
        cv2.imshow('RealSense Depth', depth_colormap)

        # 按下 'q' 键退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # 停止串流
    pipeline.stop()

    # 关闭socket连接
    sock.close()
    
    # 关闭所有OpenCV窗口
    cv2.destroyAllWindows()
