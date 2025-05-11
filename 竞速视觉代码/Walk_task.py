import cv2 as cv
import numpy as np
import math

state='\r\n'
center_now = 320
# xin
# x2,y2=175,40
# left_point=[55,150]#275
# right_point=[270,150]


x2,y2 = 175, 40
left_point=[55,150]#275
right_point=[270,150]

# x2,y2=320,50q
# left_point=[110,280]#275
# right_point=[530,280]
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
    # 余弦定理求夹角
    A=DIST(p1,p2)
    B=DIST(p2,p3)
    C=DIST(p1,p3)

    angle=math.acos((A*A+B*B-C*C)/(2*A*B))
    return angle/math.pi*180


def HSV(frame):
    '''
    识别红色虚线框
    '''
    # 在彩色图像的情况下，解码图像将以b g r顺序存储通道。
    grid_RGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    # 从RGB色彩空间转换到HSV色彩空间
    grid_HSV = cv.cvtColor(grid_RGB, cv.COLOR_RGB2HSV)

    # H、S、V范围一：
    lower1 = np.array([30,33,16])
    upper1 = np.array([124,255,181])
    mask1 = cv.inRange(grid_HSV, lower1, upper1)       # mask1 为二值图像
    res1 = cv.bitwise_and(grid_RGB, grid_RGB, mask=mask1)

    # H、S、V范围二：
    lower2 = np.array([156,43,46])
    # array是数组定义
    upper2 = np.array([180,255,255])
    mask2 = cv.inRange(grid_HSV, lower2, upper2)
    # 实现二值化功能，设置相应的阈值，去除背景（不需要的部分），为黑色；得到想要的区域，为白色。
    res2 = cv.bitwise_and(grid_RGB,grid_RGB, mask=mask2)

    # 将两个二值图像结果 相加
    mask3 = mask1 + mask2
    # 取出第320列的像素值
    cl=mask3[:,320]
    # 找到白色像素值的坐标
    white_index = np.where(cl == 255)
    # 求平均值
    red_flag=np.mean(white_index[0])
    
    # mask3 = cv.line(mask3, (320, 250), (320, 250), (0, 0, 255), 3)
    # 结果显示
    


    return mask3

def HSV_2(img,l1,l2,l3,h1,h2,h3):
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h_min, h_max, s_min, s_max, v_min, v_max =l1,h1,l2,h2,l3,h3
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv.inRange(imgHSV, lower, upper)
    imgResult = cv.bitwise_and(img, img, mask=mask)

    return mask



def Walk_task(dst):
    global left,right


    # 大津法二值化
    # retval, dst = cv.threshold(frame, 0, 255, cv.THRESH_OTSU)


    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # # 大津法二值化
    # retval, dst = cv.threshold(gray, 0, 255, cv.THRESH_OTSU)
    # 膨胀，白区域变大
    dst = cv.dilate(dst, None, iterations=2)
    # # 腐蚀，白区域变小
    dst = cv.erode(dst, None, iterations=6)
    # # 单看第250行的像素值s
    color = dst[y2]
    color_l=dst[left_point[1]]
    color_r=dst[right_point[1]]
    pixel=color[x2]
    pixel_left=color_l[left_point[0]]
    pixel_right=color_r[right_point[0]]

    #在对应位置画3个点
    dst = cv.line(dst, (x2, y2), (x2, y2), (0, 0, 255), 3)
    dst = cv.line(dst, (left_point[0], left_point[1]), (left_point[0], left_point[1]), (0, 0, 255), 3)
    dst = cv.line(dst, (right_point[0], right_point[1]), (right_point[0], right_point[1]), (0, 0, 255), 3)

    return dst,pixel,pixel_left,pixel_right











    