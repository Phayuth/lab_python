#Code_UDP_Stream_Device_1.py
#Run this first

import pickle
import time
import socket

ip,pt = '127.0.0.1',50505
ipd,ptd = '127.0.0.1',50506
sock = socket.socket(socket.AF_INET,SOCK_DGRAM)
sock.bind((ip,pt))

M = [0,0]

i=0
j=0

while True:
	print('Server is listening')
	data,addr=sock.recvfrom(2048)
	load = pickle.loads(data)
	print(f'data = {load}')
	M[0]=i
	M[1]=j
	i+=1
	j+=1
	ME=pickle.dumps(M)
	sock.sendto(ME,(ipd,ptd))
	time.sleep(0.01)