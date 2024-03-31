#Real-Time QR Code Scanner with Visual Detection and Output Actions
from time import sleep
from imutils.video import VideoStream
from pyzbar import pyzbar
import imutils
import time
import cv2
import os,sys
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)
while True:
    frame = vs.read()
    frame = imutils.resize(frame,width=400)
    QRcodes = pyzbar.decode(frame)
    for QRcodes in QRcodes:
        (x,y,w,h) = QRcodes.rect
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        QRcodeData = QRcodes.data.decode("utf-8")
        QRcodeType = QRcodes.type
        text="{}".format(QRcodeData)
        cv2.putText(frame,text,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
        if QRcodeData=='open':
            print("open")
        else:
            print("stop")
    cv2.imshow("QRcode Scanner",frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
cv2.destroyAllWindows()
vs.stop()
    
