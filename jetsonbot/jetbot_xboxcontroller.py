from jetbot import Robot
import xbox
import time

# init instance
robot = Robot()
joy = xbox.Joystick()


# Format floating point number to string format -x.xxx
def fmtFloat(n):
    return "{:6.3f}".format(n)


# Print one or more values without a line feed
def show(*args):
    for arg in args:
        print(arg, end="")


# Print true or false value based on a boolean, without linefeed
def showIf(boolean, ifTrue, ifFalse=" "):
    if boolean:
        show(ifTrue)
    else:
        show(ifFalse)


while not joy.Back():
    # connection confirm
    # show connection status
    show("Connected:")
    showIf(joy.connected(), "Y", "N")
    trigL = joy.leftTrigger()
    trigR = joy.rightTrigger()
    joyLX = joy.leftX()
    joyLY = joy.leftY()
    joyRX = joy.rightX()
    joyRY = joy.rightY()
    # Left analog stick
    show("L.Y:", fmtFloat(joy.leftY()))
    # Right analog stick
    show("R.Y:", fmtFloat(joy.rightY()))
    # Right trigger
    show("R.Tr:", fmtFloat(joy.rightTrigger()))
    # Left trigger
    show("L.Tr:", fmtFloat(joy.leftTrigger()))
    # A/B/X/Y buttons
    show("  Buttons:")
    showIf(joy.A(), "A")
    showIf(joy.B(), "B")
    showIf(joy.X(), "X")
    showIf(joy.Y(), "Y")
    # Dpad U/D/L/R
    show("  Dpad:")
    showIf(joy.dpadUp(), "U")
    showIf(joy.dpadDown(), "D")
    showIf(joy.dpadLeft(), "L")
    showIf(joy.dpadRight(), "R")
    # Move cursor back to start of line
    show(chr(13))
    # print(f'Left Trigger value = {trigL},Right Trigger value = {trigR}')
    if trigR != 0:
        if trigL == 0:
            robot.left_motor.value = joyLY
            robot.right_motor.value = joyRY
            time.sleep(0.1)
        elif trigL != 0:
            if joy.dpadUp() == 1:
                robot.left_motor.value = trigL
                robot.right_motor.value = trigL
                time.sleep(0.1)
            elif joy.dpadDown() == 1:
                robot.left_motor.value = -trigL
                robot.right_motor.value = -trigL
                time.sleep(0.1)
            elif joy.dpadLeft() == 1:
                robot.left_motor.value = -trigL
                robot.right_motor.value = trigL
                time.sleep(0.1)
            elif joy.dpadRight() == 1:
                robot.left_motor.value = trigL
                robot.right_motor.value = -trigL
                time.sleep(0.1)
            else:
                pass
    else:
        robot.left_motor.value = 0
        robot.right_motor.value = 0
        time.sleep(0.1)

# close out when done
joy.close()
