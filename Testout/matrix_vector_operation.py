import numpy as np


x = np.array([[2],[4],[6]])
b = np.array([[4],[2],[8]])
A = np.array([[2,2,2],[2,2,2],[2,2,2]])

g = np.transpose(b) @ A @ x
h = np.transpose(x) @ A @ b

print(g)
print(h)


i = np.transpose(b) @ np.transpose(A) @ A @ x
j = np.transpose(x) @ np.transpose(A) @ A @ b


print(i)
print(j)