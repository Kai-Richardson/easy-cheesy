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
