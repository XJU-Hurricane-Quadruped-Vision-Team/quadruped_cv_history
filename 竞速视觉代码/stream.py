import cv2
import Walk_task as wt
def get_point(event, x, y, flags, param):
    # 鼠标单击事件
    if event == cv2.EVENT_LBUTTONDOWN:
        # 输出坐标
        print('坐标值: ', x, y)
        # 在传入参数图像上画出该点
        #cv2.circle(param, (x, y), 1, (255, 255, 255), thickness=-1)
        img = param.copy()
        # 显示坐标与像素
        text = "("+str(x)+','+str(y)+')'+str(param[y][x])
        cv2.putText(img,text,(0,param.shape[0]),cv2.FONT_HERSHEY_PLAIN,1.5,(0,0,255),1)



if __name__ == "__main__":
    # 定义两幅图像

    # image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cap = cv2.VideoCapture(0)
    # 定义两个窗口 并绑定事件 传入各自对应的参数
    cv2.namedWindow('image')


    # 显示图像
    while(True):
        ret, frame = cap.read()
        cv2.setMouseCallback('image', get_point, frame)

        framek = wt.HSV_2(frame, 31, 0, 0, 179, 255, 255)
        cv2.imshow('image', framek)
        if cv2.waitKey(20) & 0xFF == 27:
            break

