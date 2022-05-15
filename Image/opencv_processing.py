import cv2
import numpy as np

img = cv2.imread('test.png') # Read Image

kernel = np.ones((5,5),np.uint8)

# Processing Image Here
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)          # Convert to Gray
imgBlur=cv2.GaussianBlur(imgGray,(7,7),5)             # Convert to Blur
imgED  =cv2.Canny(imgBlur,150,100)                    # Detect Edges in Image
imgDia =cv2.dilate(imgED,kernel,iterations=1)         # Dialation = for increase thickness of edge
imgEro =cv2.erode(imgDia,kernel,iterations=1)         # Dialation = for decrease thickness of edge

# Show Image Here
cv2.imshow("Image",img)
cv2.imshow("Image Gray",imgGray)
cv2.imshow("Image Blur",imgBlur)
cv2.imshow("Image ED",imgED)
cv2.imshow("Image Dia",imgDia)
cv2.imshow("Image Ero",imgEro)

# Waitkey to stop
cv2.waitKey(0)