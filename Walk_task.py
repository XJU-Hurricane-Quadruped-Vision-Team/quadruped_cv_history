import cv2 as cv
import numpy as np
import math

center_now = 320
x1,y1=320,400
x2,y2=320,250
x3,y3=0,400
p1=[x1,y1]
p2=[x2,y2]
p3=[x3,y3]
def DIST(p1,p2):
    '''
    func:求两点间距离
    @para p1,p2:点坐标(x1,y1),(x2,y2)
    @para return:距离
    '''
    return math.sqrt((p1[0]-p2[0])*(p1[0]-p2[0])+(p1[1]-p2[1])*(p1[1]-p2[1]))

def GetAngle(p1,p2,p3):
    """
    若已知3点,求以中间点为原点的夹角
    :param p1,p2,p3:点坐标(x,y)
    :param return: 角度
    """
    #余弦定理求夹角
    A=DIST(p1,p2)
    B=DIST(p2,p3)
    C=DIST(p1,p3)

    angle=math.acos((A*A+B*B-C*C)/(2*A*B))
    return angle/math.pi*180

def Filter_out_anomalous_data(current_angle,last_angle):
    """
    滤除跳变值
    """
    avg=(current_angle+last_angle)/2




def HSV(frame):
    '''
    识别红色虚线框
    '''
    # 在彩色图像的情况下，解码图像将以b g r顺序存储通道。
    grid_RGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    # 从RGB色彩空间转换到HSV色彩空间
    grid_HSV = cv.cvtColor(grid_RGB, cv.COLOR_RGB2HSV)

    # H、S、V范围一：
    lower1 = np.array([0,43,46])
    upper1 = np.array([10,255,255])
    mask1 = cv.inRange(grid_HSV, lower1, upper1)       # mask1 为二值图像
    res1 = cv.bitwise_and(grid_RGB, grid_RGB, mask=mask1)

    # H、S、V范围二：
    lower2 = np.array([156,43,46])
    upper2 = np.array([180,255,255])
    mask2 = cv.inRange(grid_HSV, lower2, upper2)
    res2 = cv.bitwise_and(grid_RGB,grid_RGB, mask=mask2)

    # 将两个二值图像结果 相加
    mask3 = mask1 + mask2
    # 取出第320列的像素值
    cl=mask3[:,320]
    #找到白色像素值的坐标
    white_index = np.where(cl == 255)
    #求平均值
    avg=np.mean(white_index[0])
    print(avg)
    mask3 = cv.line(mask3, (320, 250), (320, 250), (0, 0, 255), 3)
    # 结果显示
    # cv.imshow("img",img)
    # cv.imshow("Mask1",mask1)
    # cv.imshow("res1",res1)
    # cv.imshow("Mask2",mask2)
    # cv.imshow("res2",res2)
    # cv.imshow("grid_RGB", grid_RGB[:,:,::-1])           # imshow()函数传入的变量也要为b g r通道顺序



    return mask3




def Walk_task(frame,center_now):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # 大津法二值化
    retval, dst = cv.threshold(gray, 0, 255, cv.THRESH_OTSU)
    # 膨胀，白区域变大
    dst = cv.dilate(dst, None, iterations=2)
    # # 腐蚀，白区域变小
    dst = cv.erode(dst, None, iterations=6)
    # # 单看第250行的像素值s
    color = dst[250]
    # 找到白色的像素点个数
    white_count = np.sum(color == 255)
    # # 找到白色的像素点索引
    white_index = np.where(color == 255)
    
    # # 防止white_count=0的报错
    if white_count !=0:
    # 找到黑色像素的中心点位置
        center_now = (white_index[0][white_count - 1] + white_index[0][0]) / 2
    # 计算出center_now与标准中心点的偏移量
    direction = center_now - 320
    p3[0]=int(x1+direction)
    # 计算p1 p2 p3 三点夹角
    angle=GetAngle(p1,p2,p3)
   

    # print('计算标准中心点的偏移量:',center_now)
    dst = cv.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
    dst = cv.line(frame, (x1, y1), (int(x1+direction), y2), (0, 0, 255), 3)
    
    print('三点夹角:',angle)

    # print('计算标准中心点的偏移量:',direction)
    return dst,color[320],direction,angle

def jiaodainjiance(frame):
    '''
    官方例程
    角点检测
    '''
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv.cornerHarris(gray,2,3,0.04)
    #result is dilated for marking the corners, not important
    dst = cv.dilate(dst,None)
    # Threshold for an optimal value, it may vary depending on the image.
    frame[dst>0.01*dst.max()]=[0,0,255]
    return frame










    