import cv2 as cv                                                        ## import library 

cap = cv.VideoCapture('C:\\Users\\pc cam\\Desktop\\drone vids\\1.mp4')  ##  read/fetch the video 

def resize_video(frame, scale=0.2):                                     ## function to recize the video 
    width = int(frame.shape[1] * scale)                                 # shape[1] =width 
    height = int(frame.shape[0] * scale)                                # shape[0] = height  
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)    # resize is a method in cv library 

while True :
    
    istrue , frame =  cap.read()

    frame_resized = resize_video(frame)
    cv.imshow("drone", frame_resized)

    if cv.waitKey(20) & 0xFF == ord("d"):
        break

cap.release()
cv.destroyAllWindows
