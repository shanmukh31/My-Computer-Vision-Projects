import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:
  ret, frame = cap.read()
  frame = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
  image_array = np.array(frame)
  average_color = np.average(image_array, axis=(0, 1))
  average_color = np.round(average_color).astype(np.uint8)
  print(f"Average Color: (R, G, B) = {average_color[0]}, {average_color[1]}, {average_color[2]}")
  if cv2.waitKey(1) == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()
