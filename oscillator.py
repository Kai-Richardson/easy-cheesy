from gpiozero import AngularServo
from time import sleep

# GPIO 18 (physical pin 12)
servo = AngularServo(18, min_angle=-90, max_angle=90)
print("This is servo: ", servo)

# Move from -90° → +90° and back once
for angle in range(-90, 91, 30):
    servo.angle = angle
    sleep(0.5)

print("Completed first rotation.")

for angle in range(90, -91, -30):
    servo.angle = angle
    sleep(0.5)
print("Completed second rotation.")

servo.angle = 0  # center
sleep(1)
