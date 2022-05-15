import math
import time
import rcpy
import rcpy.motor as motor
import rcpy.encoder as encoder

m2 = motor.motor2
e2 = encoder.encoder2

# K gain
Kp = 0.01
Ki = 0
Kd = 0

#Variable PID
Pre_error = 0
Cur_error = 0
Area_old  = 0
Ts = 0.02
time_step = 0

rcpy.set_state(rcpy.RUNNING)

#Motor Parameter
#PPR = 17
#Gear_ratio = 29
tick_desired = 10000

try:
    while True:
        tick_current = e2.get()
        Cur_error = tick_current - (-tick_desired)
        pwm = Kp*Cur_error + Kd*(Cur_error - Pre_error)/Ts + Ki*(Area_old + Cur_error*Ts)
        m2.set(pwm)
        Area_old = Area_old + Cur_error*Ts
        Pre_error = Cur_error
        print(f'err={Cur_error}, pwm={pwm}, tss={time_step}')
        time_step += 1
        time.sleep(Ts)
except KeyboardInterrupt:
    # Catch Ctrl-C
    print("Done Recived and Control")
    rcpy.set_state(rcpy.EXITING)

finally:
    print("\nBye BeagleBone!")
