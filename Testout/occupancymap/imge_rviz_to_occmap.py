import cv2
import numpy as np

imgnormal = cv2.imread("saved.png")
#imgnormal = cv2.imread("imge_rviz_to_occmap_src.png")

img=cv2.cvtColor(imgnormal,cv2.COLOR_BGR2GRAY) # 0 is black , 255 is white
height, width = img.shape

loc1=(90,90) # unkown
loc2=(160,144) # black
loc3=(240,240) # white

# ls = []
# maze=[]

# proprocessing
# for i in range(height):
# 	for j in range(width):
# 		if img[i,j] < 100:
# 			img[i,j] = 0
# 		elif img[i,j] < 192:
# 			img[i,j] = 1



# invert color
for i in range(height):
	for j in range(width):
		if img[i,j] == 255:
			img[i,j] = 0
		elif img[i,j] == 0:
			img[i,j] = 255



cv2.imshow("img",img)
cv2.waitKey(0)