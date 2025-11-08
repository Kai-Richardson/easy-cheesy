from gpiozero import Button
# from carousel import rotate_to_next_slice  # TBD
from oscillator import scrape_cheese
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
    print("🧀 CheeseBot 3000 is online. Press the button to dispense a slice of cheese.")

    try:
        while True:
            button.wait_for_press()  # wait for button press
            print(f"\nButton pressed — dispensing slice #{slice_count}...\n")
            time.sleep(0.2)  # debounce delay

            # Run dispensing sequence
            # rotate_to_next_slice(slice_count)  # Uncomment when carousel is ready
            scrape_cheese()

            print(f"Slice #{slice_count} dispensed! Waiting for next button press...\n")
            slice_count += 1  # increment slice counter

    except KeyboardInterrupt:
        print("\nInterrupted. Shutting down CheeseBot safely.")

if __name__ == "__main__":
    main()
