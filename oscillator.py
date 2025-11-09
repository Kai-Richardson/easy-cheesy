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
    oscillation_speed = 0.5  # seconds between moves
    run_time = 10.0      # total time to oscillate (seconds)

    start = time()

    while time() - start < run_time:
        servo.angle = up_angle
        sleep(oscillation_speed)
        servo.angle = down_angle
        sleep(oscillation_speed)

    sleep(2)
    servo.value = 0
    sleep(3)
    

