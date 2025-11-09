import threading
import time

class BuzzerController:
    def __init__(self, buzzer):
        self.buzzer = buzzer
        self._thread = None
        self._stop_event = threading.Event()

    def _advance_cheese_thread(self, volume):
        if not self.buzzer.begin():
            print("Buzzer not connected.")
            return

        notes = [600, 750, 900, 1050, 1250, 1400]
        for freq in notes:
            if self._stop_event.is_set():
                break
            self.buzzer.configure(freq, 0, volume)
            self.buzzer.on()
            time.sleep(0.1)
            self.buzzer.off()
            time.sleep(0.05)

        flourish = [1600, 1800, 2000]
        for freq in flourish:
            if self._stop_event.is_set():
                break
            self.buzzer.configure(freq, 0, volume)
            self.buzzer.on()
            time.sleep(0.07)
            self.buzzer.off()
            time.sleep(0.03)

        # cute final ding
        if not self._stop_event.is_set():
            self.buzzer.configure(2200, 0, volume)
            self.buzzer.on()
            time.sleep(0.12)
            self.buzzer.off()

    def _cheesed_thread(self, volume):
        if not self.buzzer.begin():
            print("Buzzer not connected.")
            return

        melody = [
            (self.buzzer.NOTE_C4, 0.2),
            (self.buzzer.NOTE_D4, 0.2),
            (self.buzzer.NOTE_E4, 0.2),
            (self.buzzer.NOTE_C4, 0.2),
            (self.buzzer.NOTE_E4, 0.2),
            (self.buzzer.NOTE_G4, 0.2),
            (self.buzzer.NOTE_C5, 0.3),
        ]

        for freq, dur in melody:
            if self._stop_event.is_set():
                break
            self.buzzer.configure(freq, 0, volume)
            self.buzzer.on()
            time.sleep(dur)
            self.buzzer.off()
            time.sleep(0.05)

        if self._stop_event.is_set():
            return

        time.sleep(0.5)  # dramatic pause

        # playful up-down siren
        for note in range(400, 1800, 100):
            if self._stop_event.is_set():
                break
            self.buzzer.configure(note, 0, volume)
            self.buzzer.on()
            time.sleep(0.03)
        for note in range(1800, 400, -120):
            if self._stop_event.is_set():
                break
            self.buzzer.configure(note, 0, volume)
            self.buzzer.on()
            time.sleep(0.03)
        self.buzzer.off()

        if self._stop_event.is_set():
            return

        # final short buzz
        self.buzzer.configure(self.buzzer.NOTE_C5, 200, volume)
        self.buzzer.on()
        time.sleep(0.2)
        self.buzzer.off()

    def start_advance_cheese(self, volume=None):
        self.stop()
        self._stop_event.clear()
        self._thread = threading.Thread(
            target=self._advance_cheese_thread,
            args=(volume or self.buzzer.VOLUME_MAX)
        )
        self._thread.start()

    def start_cheesed(self, volume=None):
        self.stop()
        self._stop_event.clear()
        self._thread = threading.Thread(
            target=self._cheesed_thread,
            args=(volume or self.buzzer.VOLUME_MAX)
        )
        self._thread.start()

    def stop(self):
        if self._thread and self._thread.is_alive():
            self._stop_event.set()
            self._thread.join()
        self._thread = None
