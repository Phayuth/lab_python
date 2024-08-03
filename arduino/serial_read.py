import serial
import time


def initConnection(PortNum, baudRate):
    try:
        ser = serial.Serial(PortNum, baudRate)
        print("Device Connected")
        return ser
    except:
        print("Unable to Connect")


def sendData(se, data, digits):
    myString = "$"
    for d in data:
        myString += str(d).zfill(digits)
    try:
        se.write(myString.encode())
        print(myString)
    except:
        print("Send failed")


if __name__ == "__main__":
    # ser = initConnection("/dev/ttyACM0",9600)
    ser = initConnection("COM3", 9600)
    while True:
        sendData(ser, [0, 255], 3)
        time.sleep(1)
        sendData(ser, [0, 0], 3)
        time.sleep(1)
