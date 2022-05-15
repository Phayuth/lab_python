# test angle wrap to pi only -->only hold for angle from 0 to 2pi<--
import math

def angnorm(theta):
	if theta>0:
		if theta>math.pi:
			theta = (2*math.pi-theta)*(-1)

	if theta<0:
		if theta*(-1)>math.pi:
			theta = (2*math.pi-(-theta))*(-1)

	return theta

print(angnorm(0))