import cv2
import numpy as np
#讀取圖像
img = cv2.imread(r'D:\base\cat.jpg')
#模糊化原圖像
#blur = cv2.blur(img, (5, 5))
kernel = np.array([[-1,-1,-1],
                   [-1, 9,-1],
                   [-1,-1,-1]])
sharpen = cv2.filter2D(img, -1, kernel)
#顯示原圖像及模糊、銳化後圖像
cv2.imshow('Original', img)
#cv2.imshow('blur', blur)
cv2.imshow('sharpen', sharpen)
#關閉所有 OpenCV 視窗
cv2.waitKey(0)
cv2.destroyAllWindows()

