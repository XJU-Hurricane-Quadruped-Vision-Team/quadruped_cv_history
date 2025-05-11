import numpy as np
import cv2 
import SUN as sun

cap = cv2.VideoCapture(0)
while(True):
    # 一帧一帧捕捉
    ret, frame = cap.read()
    
    # 我们对帧的操作在这里
    mask=sun.create_mask(frame)

    mask = cv2.cvtColor(mask,  cv2.IMREAD_GRAYSCALE)

    res_ = cv2.resize(frame,None,fx=0.6, fy=0.6, interpolation = cv2.INTER_CUBIC)
    mask = cv2.resize(mask,None,fx=0.6, fy=0.6, interpolation = cv2.INTER_CUBIC)
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    
    dst = cv2.inpaint(res_, mask, 10, cv2.INPAINT_TELEA)

    # dst =sun.xiufu(frame,mask)
    # 显示返回的每帧
    cv2.imshow('frame',frame)
    cv2.imshow('DST',dst)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# 当所有事完成，释放 VideoCapture 对象
cap.release()
cv2.destroyAllWindows()
