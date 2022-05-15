import math
import numpy as np


n = 150
T = 150

times = np.linspace(0.,T,n)
print(times)
print(times[0:len(times)])
print(list(times))

# print(np.random.normal(0,0.1))


# print(np.random.randn(2, 1))


print((np.diag([1.0, np.deg2rad(30.0)]) ** 2) @ np.random.randn(2, 1))