import cv2
import numpy as np

img = cv2.imread("imge_to_occmap_src.png")
imgnormal = cv2.imread("imge_to_occmap_src.png")

img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # 0 is black , 255 is white
height, width = img.shape

ls = []
maze=[]

for i in range(height):
	for j in range(width):
		if img[i,j] == 255:
			img[i,j] = 0
		elif img[i,j] == 0:
			img[i,j] = 1
		ls.append(img[i,j])

f = 0
for k in range(height):
	print(ls[0:199])
	maze.append(ls[f:f+height])
	f+=height

print(maze)
cv2.imshow("imgnormal",imgnormal)
cv2.waitKey(0)