import time
import math
import json

import rcpy
import rcpy.motor as motor
import rcpy.encoder as encoder

rcpy.set_state(rcpy.RUNNING)  # set rcpy state to running

motor = motor.motor2
encoder = encoder.encoder2

stage = 0
motorset = 5
motor_pwm = [
    0,
    0.05,
    0.10,
    0.15,
    0.20,
    0.25,
    0.30,
    0.35,
    0.40,
    0.45,
    0.50,
    0.55,
    0.60,
    0.65,
    0.70,
    0.75,
    0.80,
    0.85,
    0.90,
    0.95,
    1,
]
motor_spd = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
old_enc = 0
Ts = 1

for i in motor_pwm:
    for j in range(0, 10):
        if motorset != i:
            print("New Stage Setted")
            motorset = i
            motor.set(i)
        print(f"PWM = {i},Timers = {j}")
        ne = encoder.get()
        spd = (ne - old_enc) / Ts
        old_enc = ne
        time.sleep(Ts)
    motor_spd[stage] = spd
    print(f"stage = {stage}")
    stage += 1
    time.sleep(Ts)


print(motor_spd)
motor.free_spin()
with open("test.txt", "w") as f:
    f.write(json.dumps(motor_pwm))
    f.write(json.dumps(motor_spd))
