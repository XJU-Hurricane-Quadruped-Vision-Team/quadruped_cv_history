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

import cv2 as cv
import serial_port
import time
import unet
import xunji
import jiance
from xunji import ser

last_state = '1'
current_state = '1'
start = False


if __name__ == '__main__':
    # 打开串口

    ser = xunji.ser

    while (start == False):
        is_start = input("输入以开始")
        if is_start == 'start':
            ser.send("ss\r\n")
            print("START")
        elif is_start == "break":
            start = True
            break
    T1 = time.time()
    flag = T1
    center = (640, 480)

    unet = unet.Unet()




    while (True):
        xunji.xunji()
        jiance.jiance()

        if cv.waitKey(1) & 0xFF == ord('q'):
            T2 = time.time()
            print(T2 - T1)
            ser.send('pp\r\n')
            print("STOP")
            break
        # print(color)
        # 显示返回的每帧
    # 当所有事完成，释放 VideoCapture 对象
    xunji.xunji_release()
    jiance.jiance_release()
    cv.destroyAllWindows()
