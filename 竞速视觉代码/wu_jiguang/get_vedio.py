
# 录制视频

import cv2

cap = cv2.VideoCapture(1)  # 设置摄像头端口
widght = int(cap.get(3))  # 在视频流的帧的宽度,3为编号，不能改
height = int(cap.get(4))  # 在视频流的帧的高度,4为编号，不能改
size = (widght, height)
fps = 30  # 帧率
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')  # 为视频编码方式，保存为mp4文
out = cv2.VideoWriter()
# 定义一个视频存储对象，以及视频编码方式,帧率，视频大小格式
out.open("C:\\Users\Redham\Desktop\shi_jue\shi_jue\wu_jiguang\\normal_chair.mp4", fourcc, fps, size)
while True:
    ref, frame = cap.read()  # 获取每一帧
    frame = cv2.flip(frame, 1)  # 翻转

    out.write(frame)  # 保存每一帧合并成视频
    cv2.imshow("frame", frame)  # 显示视频界面

    key = cv2.waitKey(1)
    if cv2.waitKey(25) & 0xFF == ord('Q'):  # 按Q退出
        break
cap.release()  # 释放
out.release()
cv2.destroyAllWindows()
