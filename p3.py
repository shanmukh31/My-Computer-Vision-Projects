import cv2
import numpy
video = cv2.VideoCapture(0)
while True:
    ret, img = video.read()
    cv2.imshow('original color video',img)
    frame=cv2.resize(img,(350,350))
    cv2.imshow('resized frame',img)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray scale converted!',gray)
    ret,bw=cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
    cv2.imshow('black and white',bw)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
