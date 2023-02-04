# Horse Racing
import math
import random

class horse:
	def __init__(self):
		self.speed = 10
		self.a_pose = 0
		self.b_pose = 0
		self.c_pose = 0
		self.d_pose = 0
	def move(self):
		return self.speed+random.randint(0, 9)


def race():
	hor=horse()
	#pick = input("Please Input your Horse Color You want to bet : ")
	#pick color go into function
	print("Racing....")
	for i in range(0,100):
		hor.a_pose = hor.a_pose + hor.move()
		hor.b_pose = hor.b_pose + hor.move()
		hor.c_pose = hor.c_pose + hor.move()
		hor.d_pose = hor.d_pose + hor.move()
	print(hor.a_pose,hor.b_pose,hor.c_pose,hor.d_pose)
race()