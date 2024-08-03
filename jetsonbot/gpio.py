import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  # internal pin number not external


class LED:
    def __init__(self, R, G, B):
        self.R = R
        self.B = B
        self.G = G
        GPIO.setup(self.R, GPIO.OUT)
        GPIO.setup(self.B, GPIO.OUT)
        GPIO.setup(self.G, GPIO.OUT)

    def color(self, controlcolor):
        if controlcolor == "red":
            GPIO.output(self.R, GPIO.LOW)
            GPIO.output(self.B, GPIO.HIGH)
            GPIO.output(self.G, GPIO.HIGH)
        elif controlcolor == "blue":
            GPIO.output(self.R, GPIO.HIGH)
            GPIO.output(self.B, GPIO.LOW)
            GPIO.output(self.G, GPIO.HIGH)
        elif controlcolor == "green":
            GPIO.output(self.R, GPIO.HIGH)
            GPIO.output(self.B, GPIO.HIGH)
            GPIO.output(self.G, GPIO.LOW)
        elif controlcolor == "off":
            GPIO.output(self.R, GPIO.HIGH)
            GPIO.output(self.B, GPIO.HIGH)
            GPIO.output(self.G, GPIO.HIGH)


def main():
    myl = LED(17, 27, 22)
    while True:
        myl.controlcolor("red")


if __name__ == "__main__":
    main()
