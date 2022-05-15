# Code_BBB_GPS_data - GY-NEO6MV2
# allow read on port : sudo chmod 666 /dev/ttys0
import serial
from time import sleep
import sys

ser = serial.Serial ("/dev/ttyS0")
try:
	while True:
		received_data = (str)(ser.readline()) #read NMEA string received
		print(received_data,'\n')
except KeyboardInterrupt:
	sys.exit(0)