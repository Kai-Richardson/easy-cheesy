from gpiozero import Button
#from carousel import rotate_to_next_slice #TBD
from oscillator import scrape_cheese
import time

# ----------------------------
# Configuration
# ----------------------------
BUTTON_PIN = 17  # GPIO pin connected to start button

# ----------------------------
# Cheese dispensing logic
# ----------------------------
def dispense_cheese(slices: int):
    print(f"\n🤖 Dispensing {slices} cheese slice{'s' if slices != 1 else ''}...")
    for i in range(1, slices + 1):
        print(f"🧩 Starting sequence for slice {i}...")
        #rotate_to_next_slice(i)
        scrape_cheese()
        print(f"--- Slice {i} complete ---\n")
        time.sleep(0.5)
    print("🍔 All slices successfully dispensed!\n")

# ----------------------------
# Main control flow
# ----------------------------
def main():
    button = Button(BUTTON_PIN)
    print("🧀 CheeseBot 3000 is online. Waiting for button press to start...")

    while True:
        button.wait_for_press()
        print("\n📶 Button pressed — CheeseBot activated!\n")
        time.sleep(0.5)  # debounce delay

        try:
            user_input = input("Enter number of cheese slices to dispense (or 'q' to quit): ").strip()
            if user_input.lower() in ["q", "quit", "exit"]:
                print("👋 Shutting down CheeseBot.")
                break

            if not user_input.isdigit():
                print("⚠️  Invalid input. Please enter a number.\n")
                continue

            slices = int(user_input)
            dispense_cheese(slices)

            print("✅ Dispensing complete. Waiting for next button press...\n")

        except KeyboardInterrupt:
            print("\n🛑 Interrupted manually. Shutting down CheeseBot safely.")
            break

if __name__ == "__main__":
    main()