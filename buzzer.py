import qwiic_buzzer
import time
import random

buzzer = qwiic_buzzer.QwiicBuzzer()

def sound_effect_cheesed(volume=buzzer.VOLUME_MAX):
    """
    Plays a short melody followed by a "you've been cheesed" tone pattern.
     """

    melody = [
        (buzzer.NOTE_C4, 0.2),
        (buzzer.NOTE_D4, 0.2),
        (buzzer.NOTE_E4, 0.2),
        (buzzer.NOTE_C4, 0.2),
        (buzzer.NOTE_E4, 0.2),
        (buzzer.NOTE_G4, 0.2),
        (buzzer.NOTE_C5, 0.3),
    ]

        # Play main melody
    for freq, dur in melody:
        buzzer.configure(freq, 0, volume)
        buzzer.on()
        time.sleep(dur)
        buzzer.off()
        time.sleep(0.05)

    # Dramatic pause
    time.sleep(0.5)

    # “You’ve been cheesed” = playful up-down siren pattern
    for note in range(400, 1800, 100):
        buzzer.configure(note, 0, volume)
        buzzer.on()
        time.sleep(0.03)
    for note in range(1800, 400, -120):
        buzzer.configure(note, 0, volume)
        buzzer.on()
        time.sleep(0.03)
    buzzer.off()

    # Short buzz at end
    buzzer.configure(buzzer.NOTE_C5, 200, volume)
    buzzer.on()
    time.sleep(0.2)
    buzzer.off()


def advance_cheese_sound(volume=buzzer.VOLUME_MAX):
    if not buzzer.begin():
        print("Buzzer not connected.")
        return

    # Step-up tones — cheerful upward motion
    notes = [600, 800, 950, 1100, 1300]
    for freq in notes:
        buzzer.configure(freq, 0, volume)
        buzzer.on()
        time.sleep(0.12)
        buzzer.off()
        time.sleep(0.05)

    # Little “hop” at the end
    buzzer.configure(1500, 0, volume)
    buzzer.on()
    time.sleep(0.15)
    buzzer.off()
