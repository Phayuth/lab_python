#! /usr/bin/env python

import rospy                               # import rospy lib for ROS
from geometry_msgs.msg import Twist        # import msg type for ROS  #from [category of the msg] import [ type of the msg , type of the msg]

def twist_callback(msg):                   # create a callback function to feed into subscriber
	V = msg.linear.x                       # assign variable for msg data
	omega = msg.angular.z                  # assign variable for msg data
	print "------------------------------------------------"
    print "Linear Vel X = " + str(V)
    print "Angluar Vel Z = " + str(omega)
	rate.sleep()

rospy.init_node('rospy_sub_template')                              # init ros node - rospy.init_node('name of the node')
sub = rospy.Subscriber('/cmd_vel', Twist, twist_callback)          # init subscriber instance - instance = rospy.Subscriber('/topic_name', msg_type, callback_func)
rate = rospy.Rate(0.5)                                             # make ros run at specific rate

while not rospy.is_shutdown():                                     # loop
	rate.sleep()