#Image to String QR Codes Generator (with Visual Display)
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pyqrcode
s = cv2.imread("C:\\Users\\Usha\\OneDrive\\Documents\\Desktop\\output.png")
img_vec = np.array2string(s)
url = pyqrcode.create(img_vec)
plt.imshow(img_vec)
plt.show()
url.svg("myqr.svg", scale=2)
url.png("qrcode.png", scale=3)
qr_code = cv2.imread("qrcode.png")
cv2.imshow("QR Code", qr_code)
