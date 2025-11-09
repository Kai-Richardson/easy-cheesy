from gpiozero import AngularServo
from time import sleep, time

def scrape_cheese():
    """
    Activate the cheese scraper oscillator servo.

    Moves servo between up_angle and down_angle repeatedly for a fixed run_time,
    then returns servo to neutral position.
    """
    signal = 12
    servo = AngularServo(signal, min_angle=-90, max_angle=90)

    up_angle = 30       # degrees upward
    down_angle = -30    # degrees downward
    oscillation_speed = 0.15  # seconds between moves
    run_time = 3.0      # total time to oscillate (seconds)

    start = time()

    while time() - start < run_time:
        servo.angle = up_angle
        print("Servo is up now: ", servo.angle)
        sleep(oscillation_speed)
        servo.angle = down_angle
        print("Servo is down now: ", servo.angle)
        sleep(oscillation_speed)

    # servo.ang

scrape_cheese()