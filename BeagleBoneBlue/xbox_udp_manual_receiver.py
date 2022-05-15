# Code_Xbox_UDP_manual.py

# import python Library
import pickle
import socket
from time import sleep

# import rcpy
import rcpy
import rcpy.motor as motor
import rcpy.encoder as encoder

# udp enable and binding
ip = '192.168.0.104'
pt = 50505
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((ip,pt))
#sock.settimeout(1)

# rc
rcpy.set_state(rcpy.RUNNING)                #set rcpy state to running
mL,mR = motor.motor2,motor.motor3           #set motor L and R to 2 and 3
eL,eR = encoder.encoder2,encoder.encoder3   #set encoder L and R

try:
	while rcpy.get_state() != rcpy.EXITING:
		if rcpy.get_state() == rcpy.RUNNING:
			udpdata , addr = sock.recvfrom(1024)
			data = pickle.loads(udpdata)    #load from pickle bytes
			# assign varianble to data
			dL = data[0] #duty cycle motor L
			dR = data[1] #duty cycle motor R
			TR = data[2] #Triger R Xbox
			if TR != 0:
				mL.set(dL)
				mR.set(dR)
				sleep(0.02)
			else:
				mL.free_spin()
				mR.free_spin()
			tcL = eL.get() #encoder tick count
			tcR = eR.get() #encoder tick count
			print(f'Motor L duty cycle = {dL}, Motor R duty cycle = {dR}, Encoder L = {tcL}, Encoder R = {tcR}')
		elif rcpy.get_state() == rcpy.PAUSED:
			mL.free_spin(),mR.free_spin()
		else:
			while rcpy.get_state() != rcpy.EXITING:
				sleep(1)
except KeyboardInterrupt:
	print("Done Recived and Control")
	rcpy.set_state(rcpy.EXITING)

finally:
	print("Buh Bye")