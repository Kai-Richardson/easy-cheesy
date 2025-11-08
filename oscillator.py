from gpiozero import AngularServo
from time import sleep

# GPIO 18 (physical pin 12)
servo = AngularServo(18, min_angle=-90, max_angle=90)

# Move from -90° → +90° and back once
for angle in range(-90, 91, 30):
    servo.angle = angle
    sleep(0.5)

for angle in range(90, -91, -30):
    servo.angle = angle
    sleep(0.5)

servo.angle = 0  # center
sleep(1)
