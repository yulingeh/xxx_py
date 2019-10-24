import cv2
import numpy as np
im = cv2.imread('test.jpg',cv2.COLOR_BGR2GRAY)
im_gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
v1 = cv2.Canny(im,70,150)
cv2.imshow('im_gray',im_gray)
cv2.imshow('v1',v1)
im2 = cv2.imread('test.jpg')
b, g, r = cv2.split(im2)
cv2.imshow("red", r)
cv2.waitKey(0)


