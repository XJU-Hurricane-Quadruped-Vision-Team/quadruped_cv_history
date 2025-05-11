import cv2
import yolo.detect
import os


# video_capture = cv2.VideoCapture(0)
detect_api = yolo.detect.DetectAPI(exist_ok=True)

while True:
    k = cv2.waitKey(1)
    # ret, frame = video_capture.read()
    opt = yolo.detect.parse_opt()

    yolo.detect.main(opt)



