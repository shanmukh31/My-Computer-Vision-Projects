import cv2
import png
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import pyqrcode
#string which represents the qr code
s=cv2.imread("C:\\Users\\Usha\\OneDrive\\Documents\\Desktop\\output.png")
img_str = np.array2string(s)
#generate qr code
url=pyqrcode.create(img_str)
plt.imshow(img_str)
#create and save the svg file naming "myqr.svg"
url.svg("myqr.svg",scale=2)
#create and save the png file name "myqr.svg"
url.png('qrcode.png',scale=3)
qr_code=cv2.imread('qrcode.png')
cv2.imshow('qr code',qr_code)
