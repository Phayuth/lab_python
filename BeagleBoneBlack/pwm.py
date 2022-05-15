import Adafruit_BBIO.PWM as PWM
import time

myPWM="P8_19" #myPWM="P8_13"

PWM.start(myPWM, 0, 50)

try:
    while True:
        DC = float(input("PWM"))
        PWM.set_duty_cycle(myPWM, DC)
        time.sleep(2)
except KeyboardInterrupt:
    print("End")
    PWM.stop(myPWM)
    PWM.cleanup()