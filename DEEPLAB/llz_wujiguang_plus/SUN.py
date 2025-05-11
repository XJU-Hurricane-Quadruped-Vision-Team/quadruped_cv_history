
import cv2 
import numpy as np
import os,shutil
def unevenLightCompensate(img, blockSize):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    average = np.mean(gray)

    rows_new = int(np.ceil(gray.shape[0] / blockSize))
    cols_new = int(np.ceil(gray.shape[1] / blockSize))

    blockImage = np.zeros((rows_new, cols_new), dtype=np.float32)
    for r in range(rows_new):
        for c in range(cols_new):
            rowmin = r * blockSize
            rowmax = (r + 1) * blockSize
            if (rowmax > gray.shape[0]):
                rowmax = gray.shape[0]
            colmin = c * blockSize
            colmax = (c + 1) * blockSize
            if (colmax > gray.shape[1]):
                colmax = gray.shape[1]

            imageROI = gray[rowmin:rowmax, colmin:colmax]
            temaver = np.mean(imageROI)
            blockImage[r, c] = temaver

    blockImage = blockImage - average
    blockImage2 = cv2.resize(blockImage, (gray.shape[1], gray.shape[0]), interpolation=cv2.INTER_CUBIC)
    gray2 = gray.astype(np.float32)
    dst = gray2 - blockImage2
    dst = dst.astype(np.uint8)
    dst = cv2.GaussianBlur(dst, (3, 3), 0)
    dst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)

    return dst

#找亮光位置
def create_mask(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    retval, dst = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    return dst
#修复图片
def xiufu(frame,mask):
    
    # mask = cv2.cvtColor(mask,  cv2.IMREAD_GRAYSCALE)
      #缩放因子(fx,fy)
    res_ = cv2.resize(frame,None,fx=0.6, fy=0.6, interpolation = cv2.INTER_CUBIC)
    mask = cv2.resize(mask,None,fx=0.6, fy=0.6, interpolation = cv2.INTER_CUBIC)
    # mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

    dst = cv2.inpaint(res_, mask, 10, cv2.INPAINT_TELEA)



    return dst
