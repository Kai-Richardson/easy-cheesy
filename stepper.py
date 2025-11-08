from gpiozero import PhaseEnableMotor
from time import sleep

# PHASE, ENABLE, PWM
motor = PhaseEnableMotor(phase=20, enable=21)
print("This is the motor: ", motor)

# Move forward slowly
print("Moving forward slowly")

motor.forward(1)
sleep(2)

print("Moving backward slowly")
motor.backward(1)
sleep(2)

print("Stopping motor")
motor.stop()
sleep(1)