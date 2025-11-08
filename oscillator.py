from gpiozero import AngularServo
from time import sleep

signal = 12
servo = AngularServo(signal, min_angle=-90, max_angle=90)
print("This is servo: ", servo)

# Move from -90° → +90° and back once
for angle in range(-90, 91, 30):
    print("This is the for loop in the first rotation")
    servo.angle = angle
    print("Servo angle is at: ", servo.angle)
    sleep(0.5)

print("Completed first rotation.")

for angle in range(90, -91, -30):
    print("This is the second for loop for second rotation")
    servo.angle = angle
    print("Servo angle is at: ", servo.angle)
    sleep(0.5)
print("Completed second rotation.")

servo.angle = 0  # center
sleep(1)
