import socket


def send_data():
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005
    MESSAGE_1 = b"wwe"
    MESSAGE_2 = b"wwwwwwwwww"
    print("UDP target IP: %s" % UDP_IP)
    print("UDP target port: %s" % UDP_PORT)
    print("message: %s" % MESSAGE_1)
    print("message: %s" % MESSAGE_2)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(MESSAGE_1, (UDP_IP, UDP_PORT))
    sock.sendto(MESSAGE_2, (UDP_IP, UDP_PORT))


def recv_data():
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    while True:
        data, addr = sock.recvfrom(1024)
        print("received message: %s" % data)


def send_pickle():
    # Run this first
    import pickle
    import time
    import socket

    ip, pt = "127.0.0.1", 50505
    ipd, ptd = "127.0.0.1", 50506
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, pt))

    M = [0, 0]

    i = 0
    j = 0

    while True:
        print("Server is listening")
        data, addr = sock.recvfrom(2048)
        load = pickle.loads(data)
        print(f"data = {load}")
        M[0] = i
        M[1] = j
        i += 1
        j += 1
        ME = pickle.dumps(M)
        sock.sendto(ME, (ipd, ptd))
        time.sleep(0.01)


def recv_pickle():
    import pickle
    import time
    import socket

    ip, pt = "127.0.0.1", 50506
    ipd, ptd = "127.0.0.1", 50505
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, pt))

    M = [0, 0]

    i = 0
    j = 0

    while True:
        M[0] = i
        M[1] = j
        i += 1
        j += 1
        ME = pickle.dumps(M)
        sock.sendto(ME, (ipd, ptd))
        print("Server is listening")
        data, addr = sock.recvfrom(2048)
        load = pickle.loads(data)
        print(f"data = {load}")
        time.sleep(0.01)
