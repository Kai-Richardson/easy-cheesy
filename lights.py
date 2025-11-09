import board
import neopixel


pixel_pin = board.RX  # Use GPIO 6 (or any valid pin)
num_pixels = 8

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)
pixels[0] = (10, 0, 0)
pixels[9] = (0, 10, 0)
pixels.show()


