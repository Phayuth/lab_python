from numpy import arange
from scipy.optimize import curve_fit
from matplotlib import pyplot


a = [0.0, 0.0, -267.0, -487.0, -707.0, -924.0, -1152.0, -1372.0, -1593.0, -1807.0, -2018.0, -2237.0, -2460.0, -2678.0, -2889.0, -3099.0, -3323.0, -3540.0, -3760.0, -3975.0, -4200.0]
x = [abs(ele) for ele in a]
y = [0,0.05,0.10,0.15,0.20,0.25,0.30,0.35,0.40,0.45,0.50,0.55,0.60,0.65,0.70,0.75,0.80,0.85,0.90,0.95,1]
print("x = ",x,"\ny = ",y)


def objective(x, a, b):
	return a * x + b


popt, _ = curve_fit(objective, x, y)
a, b = popt
print('y = %.5f * x + %.5f' % (a, b))


pyplot.scatter(x, y)
x_line = arange(min(x), max(x), 1)
y_line = objective(x_line, a, b)
pyplot.plot(x_line, y_line, '--', color='red')
pyplot.show()