def byte_convert():
    a = 255
    abytes = a.to_bytes(2, "big")
    print(a)
    print(type(a))
    print(abytes)
    b = a.from_bytes(abytes, "big")
    print(b)

def encode_data():
    data = "EX"
    a = data.encode('utf-8')
    b = a.decode('utf-8')
    print(a)
    print(b)