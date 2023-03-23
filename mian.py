# coding:utf-8

"""

                               _(\_/) 
                             ,((((^`\
                             ((((  (6 \ 
                          ,((((( ,    \
       ,,,_              ,(((((  /"._  ,`,
      ((((\\ ,...       ,((((   /    `-.-'
      )))  ;'    `"'"'""((((   (      
    (((  /            (((      \
      )) |                      |
     ((  |        .       '     |
     ))  \     _ '      `t   ,.')
     (   |   y;- -,-""'"-.\   \/  
    )   / ./  ) /         `\  \
        |./   ( (           / /'
        ||     \\          //'|
        ||      \\       _//'||
        ||       ))     |_/  ||
        \_\     |_/          ||
        `'"                  \_\
                             `'"
"""
import time
import cv2 as cv
import numpy as np
import serial_port as sp
import Walk_task as wt
import serial_port
def sign(x):
    if x>0:
        return 1.0
    else:
        return -1.0
# center定义
center_now = 320
# 打开摄像头，图像尺寸640*480（长*高），opencv存储值为480*640（行*列）
if __name__ == '__main__':
    #打开串口
    # ser=serial_port.Serial_port('COM7', baudrate=115200)

    cap = cv.VideoCapture(0)
    while(True):
        ret, frame = cap.read()
        #二值化赛道行走任务
        dst,color,direction,angle=wt.Walk_task(frame,center_now)
        #角点检测
        # img=wt.jiaodainjiance(frame)
        #HSV色域转换
        hsv_mask=wt.HSV(frame)
        #检测结果返回给串口控制
        # ser.ser_control(color)


        cv.imshow('frame',hsv_mask)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        # print(color)
        # 显示返回的每帧
    # 当所有事完成，释放 VideoCapture 对象

    cap.release()
    cv.destroyAllWindows()
