import math
import pickle
import socket
import time

# Define Receiver IP address and Port
ip = "192.168.0.115"
port = 50505

# Get Message
Mb4P = [0, 0, 0, 0, 0, 0, 0, 0]

# Binding Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

t = 0

while True:
	tt = time.time()
	delt= tt-t
	Mb4P[6]=t
	t = tt
	Mb4P[0]=45
	Mb4P[1]=0.5
	Mb4P[2]=math.sqrt(1+delt)
	Mb4P[3]=math.cos(delt)+math.sin(delt)
	Mb4P[4]=12
	Mb4P[5]=delt
	Mb4P[7]=tt
	Message = pickle.dumps(Mb4P)      # pickling the message
	sock.sendto(Message, (ip, port))  # send the data to the UDP
	time.sleep(0.01)
