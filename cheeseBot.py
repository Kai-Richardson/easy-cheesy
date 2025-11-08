from gpiozero import Button
# from carousel import rotate_to_next_slice  # TBD
from oscillator import scrape_cheese
from stepper import advance_cheese
import time

# ----------------------------
# Configuration
# ----------------------------
BUTTON_PIN = 17  # GPIO pin connected to start button

# ----------------------------
# Main control flow
# ----------------------------
def main():
    button = Button(BUTTON_PIN)
    slice_count = 1  # start counting slices
    busy = False     # flag to indicate if a slice is being dispensed

    print("🧀 CheeseBot 3000 is online. Press the button to dispense a slice of cheese.")

    def handle_press():
        nonlocal slice_count, busy

        if busy:
            print("⚠️  Already dispensing a slice. Please wait...")
            return

        busy = True
        print(f"\nButton pressed — dispensing slice #{slice_count}...\n")
        time.sleep(0.2)  # debounce delay

        # Run dispensing sequence
        advance_cheese()
        time.sleep(3)  # wait for cheese to advance
        scrape_cheese()

        print(f"Slice #{slice_count} dispensed! Waiting for next button press...\n")
        slice_count += 1
        busy = False

    # Attach the handler to the button press
    button.when_pressed = handle_press

    try:
        # Keep the program running
        while True:
            time.sleep(0.1)  # just to prevent high CPU usage

    except KeyboardInterrupt:
        print("\nInterrupted. Shutting down CheeseBot safely.")

if __name__ == "__main__":
    main()
