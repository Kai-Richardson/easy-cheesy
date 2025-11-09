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

# 8 microMode and 200 steps  @ 0.001 goes 1.5 inches
speed = 0.001

def advance_cheese():
    """
    Advance the cheese by one cheese.
    """
    DIR.value = False  # Set direction to forward
    for x in range(steps):
        STEP.value = True
        time.sleep(speed)
        STEP.value = False
        time.sleep(speed)