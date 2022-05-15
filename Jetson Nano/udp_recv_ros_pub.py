# Code_UDP_recv_ROS_pub.py
# import Library

import socket
import rospy
import pickle
import pickle_compat # for python 2.7 pickle patch
import math
import time

from std_msgs.msg import String

# enable pickle patch for python 2.7
pickle_compat.patch()

#udp enable and binding
ip = '192.168.0.104'
pt = 50505
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((ip,pt))

# setup ROS publisher
pub = rospy.Publisher('chatter',String,queue_size=10)
rospy.init_node('talker',anonymous=True)
rate = rospy.Rate(10) #hz

#loop
while True:
	data,addr = sock.recvfrom(1024)
	dataload = pickle.loads(data)
	x     = dataload[0]
	y     = dataload[1]
	theta = dataload[2]
	xdot  = dataload[3]
	ydot  = dataload[4]
	print(f'x = {x}\ny = {y}\ntheta = {theta}\nxdot = {xdot}\nydot = {ydot}'+'-------------------------')
	rospy.loginfo(str(dataload)) # logging info header for ROS
	pub.publish(str(dataload))   # publish ROS data to topic