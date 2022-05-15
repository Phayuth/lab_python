import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE_1 = b"wwe"
MESSAGE_2 = b"wwwwwwwwww"
print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE_1)
print("message: %s" % MESSAGE_2)
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.sendto(MESSAGE_1, (UDP_IP, UDP_PORT))
sock.sendto(MESSAGE_2, (UDP_IP, UDP_PORT))