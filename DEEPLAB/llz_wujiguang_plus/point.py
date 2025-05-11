
import cv2 as cv

def get_point(event,x,y,flags,param):
    if event==cv.EVENT_LBUTTONDOWN:
        print('坐标值',x,y)

if __name__ == "__main__":
    cap=cv.VideoCapture('111.mp4')


    while(True):
        ret, img = cap.read()
        # img = cv.imread(r'./IMG_20230216_173942.jpg', 0)  # 0是灰色，1或-1不写是彩色
        img1 = cv.resize(img, (320, 240))
        img2 = cv.dilate(img1, None, iterations=2)
        img3 = cv.erode(img2, None, iterations=6)
        cv.namedWindow('image')
        cv.setMouseCallback('image', get_point, img1)
        cv.imshow('image', img1)
        if cv.waitKey(20) & 0xFF == 27:
            break

    #cv.imshow('frame2', img3)
    cv.waitKey(0)
    cv.destroyAllWindows()


