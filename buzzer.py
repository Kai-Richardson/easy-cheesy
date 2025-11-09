import qwiic_buzzer
# import time

buzzer = qwiic_buzzer.QwiicBuzzer()

# buzzer.sound_effect_1(volume=buzzer.VOLUME_MAX)

def sound_effect_cheesed(self, volume=buzzer.VOLUME_MAX):
    """
    Plays a short melody followed by a "you've been cheesed" tone pattern.
    """

    melody = [
        (self.NOTE_C4, 0.2),
        (self.NOTE_D4, 0.2),
        (self.NOTE_E4, 0.2),
        (self.NOTE_C4, 0.2),
        (self.NOTE_E4, 0.2),
        (self.NOTE_G4, 0.2),
        (self.NOTE_C5, 0.3),
    ]

    # Play main melody
    for freq, dur in melody:
        self.configure(freq, 0, volume)
        self.on()
        time.sleep(dur)
        self.off()
        time.sleep(0.05)

    # Dramatic pause
    time.sleep(0.5)

    # “You’ve been cheesed” = playful up-down siren pattern
    for note in range(400, 1800, 100):
        self.configure(note, 0, volume)
        self.on()
        time.sleep(0.03)
    for note in range(1800, 400, -120):
        self.configure(note, 0, volume)
        self.on()
        time.sleep(0.03)
    self.off()

    # Short buzz at end
    self.configure(self.NOTE_C5, 200, volume)
    self.on()
    time.sleep(0.2)
    self.off()


sound_effect_cheesed()
