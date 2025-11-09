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
microMode = 2.5
# full rotation multiplied by the microstep divider
steps = 200 * microMode

LIMIT = 7
steps_taken = 0

# 8 microMode and 200 steps  @ 0.001 goes 1.5 inches
speed = 0.001

def advance_cheese():
    global steps_taken
    print("Current steps taken: ", steps_taken)
    """
    Advance the cheese by one cheese.
    """
    DIR.value = False  # Set direction to forward
    if steps_taken != LIMIT:
        for x in range(steps):
            print("Steps taken haven't reached the limit of 7. Steps taken: ", steps_taken, " and limit is ", LIMIT)
            STEP.value = True
            time.sleep(speed)
            STEP.value = False
            time.sleep(speed)
            print("Steps taken after this round is now: ", steps_taken)
        steps_taken += 1
