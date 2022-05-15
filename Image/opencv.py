# OpenCV

import cv2                       # Import CV library

# Still Image---------------------------------------------------------------------------
img = cv2.imread("test.png")     # Read Img
cv2.imshow("Output",img)         # Show Img
cv2.waitKey(0)                   # Tell it to close

# Video---------------------------------------------------------------------------------
Width = 640                                # Define Width
Height = 480                               # Define Height
cap = cv2.VideoCapture("test.mp4")         # Read frame from video
while True:                                # Loop through video frame
	read, img = cap.read()                 # Read
	img = cv2.resize(img,(Width,Height))   # Resize into W and H
	cv2.imshow("Video",img)                # Show Video
	if cv2.waitKey(1) & 0xFF == ord('q'):  # Break
		break

# Webcam---------------------------------------------------------------------------------
Width = 640                                # Define Width
Height = 480                               # Define Height
cap = cv2.VideoCapture(0)                  # Read frame from Camera
while True:                                # Loop through video frame
	read, img = cap.read()                 # Read
	img = cv2.resize(img,(Width,Height))   # Resize into W and H
	cv2.imshow("Video",img)                # Show Video
	if cv2.waitKey(1) & 0xFF == ord('q'):  # Break
		break