#! /usr/bin/env python

import rospy
import std_msgs.msg import String
import time

rospy.init_node('tutorial')   # Give the name of the node

publisher = rospy.Publisher('/say_hello', String, queue_size = 1)    # Crate instance of publisher
rate = rospy.Rate(3)   # 3 Hz   Give the rate at which ros publish will publish

i = 0

while not rospy.is_shutdown():
  publisher.publish('Hey open tu mor 1 = ' str(i))
  i += 1
  rate.sleep()