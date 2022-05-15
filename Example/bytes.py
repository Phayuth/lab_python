# Example_For_byting_variable.py
a = 255
abytes = a.to_bytes(2,'big')
print(a)
print(type(a))
print(abytes)
b = a.from_bytes(abytes,'big')
print(b)
