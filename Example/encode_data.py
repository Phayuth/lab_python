# Encode data to byte

data = "EX"
a = data.encode('utf-8')
b = a.decode('utf-8')

print(a)
print(b)