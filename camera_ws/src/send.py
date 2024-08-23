import cv2
import socket
import numpy as np
import struct

# 设置摄像头
cap = cv2.VideoCapture(0)

# 设置 TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('10.72.221.29', 9999)
sock.connect(server_address)

if not cap.isOpened():
    print("无法打开摄像头")
    exit()

while True:
    # 读取镜头中的画面
    ret, frame = cap.read()

    if ret:
        # 压缩图像
        encoded, buffer = cv2.imencode('.jpg', frame)
        message = buffer.tobytes()

        # 发送图像大小
        sock.sendall(struct.pack(">L", len(message)) + message)

        # 显示本地摄像头画面
        cv2.imshow('Camera Feed', frame)

        # 如果按下 'q' 键，则退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("无法读取画面")
        break

# 释放摄像头并关闭连接
cap.release()
sock.close()
cv2.destroyAllWindows()
