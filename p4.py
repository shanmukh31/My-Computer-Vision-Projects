import cv2
import png
import pyqrcode
#string which represents the qr code
s="C:\\Users\\Usha\\OneDrive\\Documents\\Desktop\\output.png"
#generate qr code
url=pyqrcode.create(s)
#create and save the svg file naming "myqr.svg"
url.svg("myqr.svg",scale=9)
#create and save the png file name "myqr.svg"
url.png('qrcode.png',scale=9)
qr_code=cv2.imread('qrcode.png')
cv2.imshow('qr code',qr_code)

#
