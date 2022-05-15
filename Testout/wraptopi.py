# wrap to pi
import math

def normalize_angle(theta):
	"""Normalize an angle theta to theta_norm so that: 0 <= theta_norm < 2 * np.pi"""
	twopi =  2*math.pi #* 2

	if theta >= twopi:
		m = math.floor(theta/twopi)
		if theta/twopi - m > 0.99999:   # account for rounding errors
			m += 1
		theta_norm = theta - m * twopi
	elif theta < 0:
		m = math.ceil(theta/twopi)
		if theta/twopi - m < -0.99999:   # account for rounding errors
			m -= 1
		theta_norm = abs(theta - m * twopi)
	else:
		theta_norm = theta
	return theta_norm


print(normalize_angle(3*math.pi))