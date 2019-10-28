import time 
import random
from neopixel import *

# LED strip configuration:
LED_COUNT = 32
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 5
LED_BRIGHTNESS = 255
LED_INVERT = False

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)

def light():
	strip.begin()
	for i in range(0, 32):
		strip.setPixelColor(i, Color(0, 255, 0))
		strip.show()

def shutdown():
	strip.begin()
	for i in range(0, 32):
		strip.setPixelColor(i, Color(0, 0, 0))
		strip.show()

def shine():
	light()
	time.sleep(1.0)
	shutdown()


if __name__ == "__main__":
	while 1:
		try:
			light()
			time.sleep(0.5)
			shutdown()
		except KeyboardInterrupt:
			shutdown()
		
