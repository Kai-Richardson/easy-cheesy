import qwiic_buzzer
import time

buzzer = qwiic_buzzer.QwiicBuzzer()

if not buzzer.is_connected():
    print("Buzzer not detected. Check I2C wiring.")
    exit()

buzzer.begin()
print("Playing tune...")

# Play C4 (262 Hz) for 500 ms
buzzer.play_tone(262, 500)
time.sleep(0.5)

# Play a short melody
notes = [262, 294, 330, 349, 392, 440, 494, 523]
for note in notes:
    buzzer.play_tone(note, 200)
    time.sleep(0.05)

buzzer.stop_tone()
print("Done!")
