#ROS tutorial 2.2: Python walkthrough of publisher/subscriber lab   https://www.youtube.com/watch?v=DLVyc9hOvk8
#!/usr/bin/env python
import math
#rospy lib import
import rospy
#from [category of the msg] import [ type of the msg , type of the msg]
from nav_msgs.msg import Odometry
from location_monitor.msg import LandmarkDistance  # this is the custom msg

def distance(x1,y1,x2,y2):
	xd = x1 - x2
	yd = y1 - y2
	return math.sqrt(xd*xd + yd*yd)

class LandmarkMonitor(object):
	def __init__(self,pub,landmarks):
		self._pub = pub
		self._landmarks = landmarks

	def callback(self.msg):
		x = msg.pose.pose.position.x              # take the data from the subscribed topic
		y = msg.pose.pose.position.y              # take the data from the subscribed topic
		rospy.loginfo('x:{},y:{}'.format(x,y))    # show log data print on the terminal
		closest_name = None
		closest_distance = None
		for l_name, l_x, l_y in self._landmarks:
			dist = distance(x,y,l_x,l_y)
			if closest_distance is None or dist<closest_distance:
				closest_name = l_name
				closest_distance = dist
		ld = LandmarkDistance()                                # create instance of the message
		ld.name = closest_name                                 # filling out the information to msg to publish
		ld.distance = closest_distance                         # filling out the information to msg to publish
		self._pub.publish(ld)
		if closest_distance < 0.5:
			rospy.loginfo('I\'m near the  : {}'.format(closest_name))  # show log data print on the terminal

def main()
	rospy.init_node('survey_loz')                             # init ros node   rospy.init_node('name of the node')

	landmarks = []                                            # create list of landmark
	landmarks.append(("cube",0.31,-0.99))                     # create list of landmark
	landmarks.append(("dump",0.11,-2.42))                     # create list of landmark
	landmarks.append(("cyld",-1.14,-2.88))                    # create list of landmark
	landmarks.append(("barr",-2.59,-0.83))                    # create list of landmark
	landmarks.append(("bksh",-0.09,0.53))                     # create list of landmark

	pub = rospy.Publisher('closet_landmark',LandmarkDistance,queue_size = 10) # init publisher  rospy.Publisher('topic_name',type of the msg)
	rospy.Subcriber('/odom',Odometry,monitor.callback)        # init subscriber rospy.Subcriber('topic_name',type of the msg ,callback_func)
	rospy.spin()                                              # loop ros 4ever until it crash or keyboard interrupt

if __name__ =='__main__':
	main()