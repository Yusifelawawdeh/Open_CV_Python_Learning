import numpy as np
import cv2

#adaptive thresholding for segmentation


img = cv2.imread("sudoku.png", 0)
cv2.imshow("Original", img)

#regular thresholding here
ret, thresh_basic = cv2.threshold(img,70,255, cv2.THRESH_BINARY)
cv2.imshow("Basic Binary", thresh_basic)

#adaptive here
thresh_adapt = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow("Adaptive", thresh_adapt)

cv2.waitKey(0)
cv2.destroyAllWindows()
