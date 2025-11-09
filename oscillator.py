from gpiozero import AngularServo
from time import sleep, time

def scrape_cheese():
    """
    Activate the cheese scraper oscillator servo.

    Moves servo between up_angle and down_angle repeatedly for a fixed run_time,
    then returns servo to neutral position.
    """
    signal = 12
    servo = AngularServo(signal, min_angle=-90, max_angle=90, min_pulse_width=0.0005,  # 0.5ms
        max_pulse_width=0.0025) 
    servo.angle = 0
    sleep(0.5) 

    up_angle = 90       # degrees upward
    down_angle = 40    # degrees downward
    oscillation_speed = 0.15  # seconds between moves
    run_time = 3.0      # total time to oscillate (seconds)

    start = time()

    while time() - start < run_time:
        servo.angle = up_angle
        sleep(oscillation_speed)
        servo.angle = down_angle
        sleep(oscillation_speed)
    
    servo.angle = 0
