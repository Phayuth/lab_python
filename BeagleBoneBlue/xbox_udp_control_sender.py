# Code_Xbox_UDP_control_sender.py

import xbox
import pickle
import socket
import time

#init instance
joy = xbox.Joystick()

#UDP bind
ip    = '192.168.0.104'
pt    = 50505
sock  = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
M     = [0,0,0] # message to send

while not joy.Back()
	trigR = joy.rightTrigger()
	joyLY = joy.leftY()
	joyRY = joy.rightY()
	M[0]  = joyLY
	M[1]  = joyRY
	M[2]  = trigR
	Mp    = pickle.dumps(M)  # pickling the message
	sock.sendto(Mp,(ip,pt))  # send the data
	time.sleep(0.02)
#close out
joy.close()