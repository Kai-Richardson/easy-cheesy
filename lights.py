import board
import neopixel
import time

pixel_pin = board.RX
num_pixels = 9

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)
pixels[0] = (10, 0, 0)
pixels[8] = (0, 10, 0)
pixels.show()

time.sleep(2)

# Proper cleanup
pixels.deinit()
del pixels
