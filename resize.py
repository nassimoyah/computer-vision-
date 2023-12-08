import cv2 as cv

img = cv.imread('C:\\Users\\pc cam\\Desktop\\rock\\1.png')

cv.imshow('hand',img)

def resc(frame,scale=0.75): 
    width = int( frame.shape[1]  * scale )
    hight = int( frame.shape[0]  * scale )
    dim = (width,hight)
    return cv.resize(frame,dim)
rf = resc(img)
cv.imshow('hand2',rf)
cv.waitKey(0)
