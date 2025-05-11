import cv2 as cv
import numpy as np
import serial_port as sp
import Walk_task as wt
import serial_port
import deeplab
import time

from PIL import Image
import cv2

import os


center = (640, 480)
ser = serial_port.Serial_port('/dev/ttyUSB0', baudrate=115200)
deeplab = deeplab.DeeplabV3()
video_save_path = 0
video_fps = 25.0
video_path = 0

capture = cv.VideoCapture(0)
# capture.set(cv.CAP_PROP_FOURCC, cv.VideoWriter_fourcc('m', 'p', '4','v'))
ret, frame = capture.read()
# if video_save_path != "":
#     # 设置视频编解码器为 mp4v
#     fourcc = cv.VideoWriter_fourcc(*'mp4v')
#     size = (int(capture.get(cv.CAP_PROP_FRAME_WIDTH)), int(capture.get(cv.CAP_PROP_FRAME_HEIGHT)))
#     out = cv.VideoWriter(video_save_path, fourcc, video_fps, size)
#     #capture.set(cv.CAP_PROP_FOURCC, cv.VideoWriter_fourcc('m', 'p', '4', 'v'))

def xunji():
    last_state = '1'
    current_state = '1'
    ret, frame = capture.read()
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    frame = Image.fromarray(np.uint8(frame))
    frame = np.array(deeplab.detect_image(frame))
    frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
    img = cv.resize(frame, (320, 320))
    # imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    # h_min, h_max, s_min, s_max, v_min, v_max = (0, 179, 75, 170, 0, 255)
    # lower = np.array([h_min, s_min, v_min])
    # upper = np.array([h_max, s_max, v_max])
    # mask = cv.inRange(imgHSV, lower, upper)
    # mask = cv.bitwise_not(mask)
    # imgResult = cv.bitwise_and(img, img, mask=mask)
    dst, color, pixel_left, pixel_right = wt.Walk_task(img)
    last_state, current_state = ser.ser_control(color,
                                                pixel_left=pixel_left,
                                                pixel_right=pixel_right,
                                                last_state=last_state,
                                                current_state=current_state)
    # print("color=")
    # print(color)
    # print("pixel_left=")
    # print(pixel_left)
    # print("pixel_right=")
    # print(pixel_right)
    frame = wt.draw_points(dst)
    cv.imshow('frame', frame)
    return capture

def xunji_release():
    capture.release()
