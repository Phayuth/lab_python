import cv2
import numpy as np

img = cv2.imread('test.png')              # Read Image
print(f'Size of the image {img.shape}')   # Show the size of the Image

# Resize Here
imgRSm = cv2.resize(img,(640,480))          # Directly resize to exact pixel
imgRSs = cv2.resize(img,(0,0),None,0.5,0.5) # Resize by scale

# Crop Here
imgCrp = img[100:200,200:300]               # Crop  [x1:x2,y1:y2] pixel
# Show Image Here
cv2.imshow('Original',img)
cv2.imshow('imgRSM',imgRSm)
cv2.imshow('imgRSS',imgRSs)
cv2.imshow('imgCRP',imgCrp)

# Waitkey to stop
cv2.waitKey(0)