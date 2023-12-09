import cv2 as cv

cap = cv.VideoCapture("C:\\Users\\pc cam\\Desktop\\drone vids\\dog.mp4")


while True :
    istrue , frame =  cap.read()
    cv.imshow("drone",frame)

    if cv.waitKey(20) & 0xFF ==ord("d"):
        break

cap.release()
cv.destroyAllWindows
