from gpiozero import AngularServo
from time import sleep, time

def scrape_cheese():
    """
    Activate the cheese scraper oscillator servo.

    Moves servo between up_angle and down_angle repeatedly for a fixed run_time,
    then returns servo to neutral position.
    """
    signal = 12
    servo = AngularServo(signal, min_pulse_width=0.0005, max_pulse_width=0.0025) 

    up_angle = 60     # degrees upward
    down_angle = 90    # degrees downward
    oscillation_speed = 0.15  # seconds between moves
    run_time = 3.0      # total time to oscillate (seconds)

    start = time()

    # 0: not moving, 1: going up, 2: going down
    direction = 0
    while time() - start < run_time:
        if direction == 0:
            direction = 1
            servo.angle = up_angle
            sleep(oscillation_speed)
            print("going up")
        elif servo.angle == up_angle:
            direction = 2
            servo.angle = down_angle
            sleep(oscillation_speed)
            print("going down")
        elif servo.angle == down_angle:
            direction = 0
            print("finished a cycle")
        
    sleep(2)
    servo.value = 0

