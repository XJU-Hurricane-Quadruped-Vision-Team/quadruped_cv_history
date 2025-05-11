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
import time
import xunji

start = False
current_state = 0

if __name__ == '__main__':
    ser = xunji.ser  # 打开串口

    while not start:
        is_start = input("输入以开始")
        if is_start == 'start':
            ser.send("ss\r\n")
            print("START")
        elif is_start == "ok":
            start = False
            break
    T1 = time.time()

    while True:
        last_state = xunji.xunji(current_state)
        current_state = last_state
        if cv.waitKey(1) & 0xFF == ord('q'):
            T2 = time.time()
            print(T2 - T1)
            ser.send('pp\r\n')
            print("STOP")
            break

    xunji.xunji_release()
    cv.destroyAllWindows()

