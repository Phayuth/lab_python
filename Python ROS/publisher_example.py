#! /usr/bin/env python

import rospy                               # import rospy lib for ROS
from sensor_msgs.msg import Imu            # import msg type for ROS  #from [category of the msg] import [ type of the msg , type of the msg]
from nav_msgs.msg import Odometry          # import msg type for ROS  #from [category of the msg] import [ type of the msg , type of the msg]

rospy.init_node('rospy_pub_template')                              # init ros node - rospy.init_node('name of the node')
pub_imu = rospy.Publisher('/imu_data', Imu, queue_size=10)          # init publisher instance - pub = rospy.Publisher('/topic_name', msg_type, queue_size=10)
pub_odom= rospy.Publisher('/odom_data', Odometry, queue_size=10)    # init publisher instance - pub = rospy.Publisher('/topic_name', msg_type, queue_size=10)

rate = rospy.Rate(0.5)                  # rate of publish Hz
while not rospy.is_shutdown():
	imu = Imu()                         # create msg instance for filling out info before publish
	imu.orientation.x = qx              # filling out the information to msg to publish
	imu.orientation.y = qy
	imu.orientation.z = qz
	imu.orientation.w = qw
	imu.angular_velocity.x = vx
	imu.angular_velocity.y = vy
	imu.angular_velocity.z = vz
	imu.linear_acceleration.x = ax
	imu.linear_acceleration.y = ay
	imu.linear_acceleration.z = az       # filling out the information to msg to publish

	odom = Odometry()                    # create msg instance for filling out info before publish
	odom.pose.pose.position.x = x        # filling out the information to msg to publish
	odom.pose.pose.position.y = y
	odom.pose.pose.position.z = z
	odom.pose.pose.orientation.x = qx
	odom.pose.pose.orientation.y = qy
	odom.pose.pose.orientation.z = qz
	odom.pose.pose.orientation.w = qw     # filling out the information to msg to publish

	pub_imu.publish(imu)                 # publish pub instance with information of msg
	pub_odom.publish(odom)               # publish pub instance with information of msg

	rate.sleep()