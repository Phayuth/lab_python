import time
import rcpy
import rcpy.encoder as encoder

rcpy.set_state(rcpy.RUNNING)
print("Press Ctrl-C to exit")

# header
print("     E2 |     E3")
try:
    # keep running
    while True:
        # running
        if rcpy.get_state() == rcpy.RUNNING:
            e2 = encoder.get(2)  # read the encoders
            e3 = encoder.get(3)
            print("\r {:+6d} | {:+6d}".format(e2, e3), end="")
        time.sleep(0.5)  # sleep some

except KeyboardInterrupt:
    # Catch Ctrl-C
    pass

finally:
    print("\nBye BeagleBone!")
