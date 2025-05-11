import cv2 as cv
import numpy as np
import mid
import serial_port
import deeplab
from PIL import Image

center = (640, 480)
ser = serial_port.Serial_port('COM22', baudrate=115200)
deeplab = deeplab.DeeplabV3()
video_save_path = 0
video_fps = 25.0
video_path = 0
capture = cv.VideoCapture(1)
ret, frame = capture.read()
img = cv.resize(frame, (320, 320))
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 使用列表 (list) 定义数组
arr = list(range(0, 319))

def xunji(last_state):
    ret, frame = capture.read()
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    frame = Image.fromarray(np.uint8(frame))
    frame = np.array(deeplab.detect_image(frame))
    frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
    img = cv.resize(frame, (320, 320))

    middle_point, middle_base, left_base, right_base, last_state = mid.middle_point(img, last_state)

    ser.ser_ctrl(middle_point=middle_point, middle_base=middle_base, left_base=left_base, right_base=right_base)
    return last_state


def xunji_release():
    capture.release()
