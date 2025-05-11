import cv2 as cv
import cv2
import yolo.detect
import os

capture = cv.VideoCapture(1)

def jiance():
    capture.set(cv.CAP_PROP_FOURCC, cv.VideoWriter_fourcc('m', 'p', '4', 'v'))  #图形优化
    ret, frame = capture.read()
    path = 'C:\\Users\Redham\Desktop\shi_jue\wu_jiguang(1)\wu_jiguang\data\myimages'
    cv2.imwrite(os.path.join(path, 'test.jpg'), frame)
    detect_api = yolo.detect.DetectAPI(exist_ok=True)
    label = detect_api.run()
    print(str(label))
    image = cv2.imread('C:\\Users\Redham\Desktop\shi_jue\wu_jiguang(1)\wu_jiguang\\runs\detect\exp\\test.jpg', flags=1)
    cv2.imshow("video", image)
    return capture

def jiance_release():
    capture.release()
