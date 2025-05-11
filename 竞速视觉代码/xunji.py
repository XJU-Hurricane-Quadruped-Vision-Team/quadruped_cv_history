import cv2 as cv
import numpy as np
import serial_port as sp
import Walk_task as wt
import serial_port
import debug as de
import time
from main import yolop
import unet
from PIL import Image
import cv2

import os


center = (640, 480)
ser = serial_port.Serial_port('COM15', baudrate=115200)
# cap = cv.VideoCapture(0)
# cap = cv.VideoCapture('day1.mp4')

unet = unet.Unet()
video_save_path = "day.mp4"
video_fps = 25.0
video_path = 0

capture = cv.VideoCapture(video_path)
capture.set(cv.CAP_PROP_FOURCC, cv.VideoWriter_fourcc('m', 'p', '4','v'))

if video_save_path != "":
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    size = (int(capture.get(cv.CAP_PROP_FRAME_WIDTH)), int(capture.get(cv.CAP_PROP_FRAME_HEIGHT)))
    out = cv.VideoWriter(video_save_path, fourcc, video_fps, size)
# capture = cv.VideoCapture(0)
# myImages
def xunji():
    last_state = '1'
    current_state = '1'
    capture.set(cv.CAP_PROP_FOURCC, cv.VideoWriter_fourcc('m', 'p', '4', 'v'))
    ret, frame = capture.read()
    # outimg = yolonet.detect(frame)
    # 格式转变，BGRtoRGB
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    # 转变成Image
    frame = Image.fromarray(np.uint8(frame))
    # 进行检测
    frame = np.array(unet.detect_image(frame))
    # RGBtoBGR满足opencv显示格式
    frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)

    img = cv.resize(frame, (320, 240))
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    # 调用回调函数，获取滑动条的值
    h_min, h_max, s_min, s_max, v_min, v_max = (0, 179, 75, 170, 0, 255)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    # 获得指定颜色范围内的掩码
    mask = cv.inRange(imgHSV, lower, upper)
    mask = cv.bitwise_not(mask)
    # 对原图图像进行按位与的操作，掩码区域保留
    imgResult = cv.bitwise_and(img, img, mask=mask)
    dst, color, pixel_left, pixel_right = wt.Walk_task(mask)
    last_state, current_state = ser.ser_control(color,
                                                pixel_left=pixel_left,
                                                pixel_right=pixel_right,
                                                last_state=last_state,
                                                current_state=current_state)
    cv.imshow('frame', dst)
    return capture

def xunji_release():
    capture.release()
