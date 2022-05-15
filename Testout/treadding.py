import threading
import time

def funx(y):
	print("startx")
	time.sleep(y)
	print("donex")

def funy(y):
	print("starty")
	time.sleep(y)
	print("doney")


x = threading.Thread(target=funx, args=(6,))
x.start()

y = threading.Thread(target=funy, args=(6,))
y.start()


x.join()
y.join()