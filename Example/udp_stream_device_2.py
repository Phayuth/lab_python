#Code_UDP_Stream_Device_2.py

import pickle
import time
import socket

ip,pt = '127.0.0.1',50506
ipd,ptd = '127.0.0.1',50505
sock = socket.socket(socket.AF_INET,SOCK_DGRAM)
sock.bind((ip,pt))

M = [0,0]

i=0
j=0

while True:
	M[0]=i
	M[1]=j
	i+=1
	j+=1
	ME=pickle.dumps(M)
	sock.sendto(ME,(ipd,ptd))
	print('Server is listening')
	data,addr=sock.recvfrom(2048)
	load = pickle.loads(data)
	print(f'data = {load}')
	time.sleep(0.01)