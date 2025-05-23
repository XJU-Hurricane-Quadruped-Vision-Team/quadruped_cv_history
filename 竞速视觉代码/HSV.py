import cv2
import numpy as np

# 创建滑动条，便于调参

# 滑动条的回调函数，获取滑动条位置处的值
def empty():
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    return h_min, h_max, s_min, s_max, v_min, v_max


path = 'Resources/11.jpg'
# 创建一个窗口，放置6个滑动条
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 75, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 170, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)
cap = cv2.VideoCapture('day_15.mp4')

# def ERZHIHUA(cap,h_min, h_max, s_min, s_max, v_min, v_max):
#     ret, img = cap.read()
#     img = cv2.resize(img, (320, 240))
#     imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#     lower = np.array([h_min, s_min, v_min])
#     upper = np.array([h_max, s_max, v_max])
#     mask = cv2.inRange(imgHSV, lower, upper)
#     return mask

while True:
    ret, img = cap.read()
    img = cv2.resize(img,(320, 240))
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # 调用回调函数，获取滑动条的值
    h_min, h_max, s_min, s_max, v_min, v_max = empty()
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    # 获得指定颜色范围内的掩码
    mask = cv2.inRange(imgHSV, lower, upper)
    # 对原图图像进行按位与的操作，掩码区域保留
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("Mask", mask)
    cv2.imshow("Result", imgResult)

    cv2.waitKey(1)
