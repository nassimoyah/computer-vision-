import numpy as np
import cv2 as cv
blank = np.zeros((500,500,3),dtype='uint8')

cv.imshow('bl',blank)

blank[0:100] = 0,255,0

cv.imshow('green',blank)

cv.waitKey(0)
