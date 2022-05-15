import numpy as np

a = np.array([[1,2,44]])

a = np.append(a, np.array([[10,20,30]]), axis=0)
a = np.append(a, np.array([[40,50,60]]), axis=0)

print(a)

b = np.array([[6]])
c = np.array([5])
print(np.shape(b))
print(np.shape(c))
