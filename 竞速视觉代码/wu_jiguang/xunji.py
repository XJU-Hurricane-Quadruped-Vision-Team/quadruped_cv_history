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


center = (80, 80)
ser = serial_port.Serial_port('COM15', baudrate=115200)
# cap = cv.VideoCapture(0)
# cap = cv.VideoCapture('day1.mp4')

unet = unet.Unet()
video_save_path = "C:\\Users\Redham\Desktop\\unet_saved_vedio\day.mp4"
video_fps = 100
# video_path = "C:\\Users\Redham\Desktop\\unet_saved_vedio\\1_11.mp4"

capture = cv.VideoCapture(0)
capture.set(cv.CAP_PROP_FOURCC, cv.VideoWriter_fourcc('m', 'p', '4','v'))


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
    #
    img = cv.resize(frame, (160, 160))
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    # 调用回调函数，获取滑动条的值
    h_min, h_max, s_min, s_max, v_min, v_max = (100, 124, 43, 255, 46, 255)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    # 获得指定颜色范围内的掩码
    mask = cv.inRange(imgHSV, lower, upper)
    mask = cv.bitwise_not(mask)
    # # 对原图图像进行按位与的操作，掩码区域保留
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

