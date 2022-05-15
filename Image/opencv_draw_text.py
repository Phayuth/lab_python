import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)   # Create image
img[:] = 255,255,255                   # Create Color Background

# Draw Here
cv2.circle(img,(256,256),120,(0,69,255),5)            # Draw circle       CV2.circle(img,(xcenter,ycenter),radius,(B,G,R),thickness<--- or cv2.FILLED)
cv2.rectangle(img,(150,222),(363,400),(222,252,22),2) # Draw rectangular  CV2.circle(img,(x1,x2),(y1,y2),(B,G,R),thickness<--- or cv2.FILLED)
cv2.line(img,(150,222),(363,400),(222,252,22),2)      # Draw line         CV2.circle(img,(x1,x2),(y1,y2),(B,G,R),thickness<--- or cv2.FILLED)
cv2.putText(img,"TESTTESTTESTTESTTEST",(139,256),cv2.FONT_HERSHEY_DUPLEX, 0.75,(0,25,251),3)


cv2.imshow("Image",img)
cv2.waitKey(0)