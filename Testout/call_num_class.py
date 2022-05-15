import numpy as np
class call():
	def __init__(self):
		self.x = 1
		self.u = 2
		self.g = np.array([12])
	def sul(self):
		self.x = 55
a = call()
print(a.g[0])
a.sul()
print(a.x)