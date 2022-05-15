import cv2

def findObj(img,objectCascade,scaleF=1.1,minN=4):
	imgObj = img.copy()
	imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	obj = objectCascade.detectMultiScale(imgGray,scaleF,minN)
	for (x,y,w,h) in obj:
		cv2.rectangle(imgObj,(x,y),(x+w,y+h),(255,0,255),2)
	return imgObj,obj

def main():
	img = cv2.imread('test.png')
	faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
	imgObj,obj = findObj(img,faceCascade)
	cv2.imshow("Out",imgObj)
	cv2.waitKey(0)

if __name__="__main__":
	main()