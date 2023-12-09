import cv2 as cv

img = cv.imread('C:\\Users\\pc cam\\Desktop\\rock\\1.png')
cv.imshow('hand',img)

def resize(frame,scale=0.75): 
    width = int( frame.shape[1]  * scale )
    hight = int( frame.shape[0]  * scale )
    dim = (width,hight)
    return cv.resize(frame,dim)
    
resized_imag=  resize(img)
cv.imshow('hand2',resized_imag)
cv.waitKey(0)
