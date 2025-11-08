import time
import board
from digitalio import DigitalInOut, Direction

# dir nd step pins as outputs
DIR = DigitalInOut(board.D20)
DIR.direction = Direction.OUTPUT
STEP = DigitalInOut(board.D21)
STEP.direction = Direction.OUTPUT

# microstep mode, default is 1/8 so 8
# another ex: 1/16 microstep would be 16
microMode = 8
# full rotation multiplied by the microstep divider
steps = 200 * microMode

while True:
    # change dir every loop
    DIR.value = not DIR.value
    print("Direction:", DIR.value)
    for x in range(steps):
        STEP.value = True
        time.sleep(0.001)
        STEP.value = False
        time.sleep(0.001)
    print("Full rotation complete")
    time.sleep(1)