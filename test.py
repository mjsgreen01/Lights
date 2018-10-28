#https://learn.adafruit.com/neopixels-on-raspberry-pi/software
#!/usr/bin/env python3# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
from neopixel import *
import argparse

# LED strip configuration:
LED_COUNT      = 150      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


'''def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(1, strip.numPixels,2()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)
		
def colorWipe2(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(0, strip.numPixels+1,2()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)	'''	


strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()




strip.setPixelColorRGB(0,0,0,255) # Blue   
strip.setPixelColorRGB(1,255,255,255) #     
strip.setPixelColorRGB(2,0,0,255) # Blue
strip.setPixelColorRGB(3,255,255,255) #   
strip.setPixelColorRGB(4,0,0,255) # Blue  
strip.setPixelColorRGB(5,255,255,255) #   
strip.setPixelColorRGB(6,0,0,255) # Blue  
strip.setPixelColorRGB(7,255,255,255) #  
strip.setPixelColorRGB(8,0,0,255) # Blue  
strip.setPixelColorRGB(9,255,255,255) #  
strip.setPixelColorRGB(10,0,0,255) # Blue  
strip.setPixelColorRGB(11,255,255,255) # 
strip.setPixelColorRGB(12,0,0,255) # Blue  
strip.setPixelColorRGB(13,255,255,255) #   
strip.setPixelColorRGB(14,0,0,255) # Blue  
strip.setPixelColorRGB(15,255,255,255) #   
strip.setPixelColorRGB(16,0,0,255) # Blue  
strip.setPixelColorRGB(17,255,255,255) #  
strip.setPixelColorRGB(18,0,0,255) # Blue  
strip.setPixelColorRGB(19,255,255,255) #  
strip.setPixelColorRGB(20,0,0,255) # Blue  
strip.setPixelColorRGB(21,255,255,255) #  
strip.setPixelColorRGB(22,0,0,255) # Blue  
strip.setPixelColorRGB(23,255,255,255) #  
strip.setPixelColorRGB(24,0,0,255) # Blue  
strip.setPixelColorRGB(25,255,255,255) #   
strip.setPixelColorRGB(26,0,0,255) # Blue  
strip.setPixelColorRGB(27,255,255,255) #   
strip.setPixelColorRGB(28,0,0,255) # Blue  
strip.setPixelColorRGB(29,255,255,255) #   
strip.setPixelColorRGB(30,0,0,255) # Blue 
strip.setPixelColorRGB(31,255,255,255) #     
strip.setPixelColorRGB(32,0,0,255) # Blue
strip.setPixelColorRGB(33,255,255,255) #   
strip.setPixelColorRGB(34,0,0,255) # Blue  
strip.setPixelColorRGB(35,255,255,255) #   
strip.setPixelColorRGB(36,0,0,255) # Blue  
strip.setPixelColorRGB(37,255,255,255) #  
strip.setPixelColorRGB(38,0,0,255) # Blue  
strip.setPixelColorRGB(39,255,255,255) #  
strip.setPixelColorRGB(40,0,0,255) # Blue  
strip.setPixelColorRGB(41,255,255,255) # 
strip.setPixelColorRGB(42,0,0,255) # Blue  
strip.setPixelColorRGB(43,255,255,255) #   
strip.setPixelColorRGB(44,0,0,255) # Blue  
strip.setPixelColorRGB(45,255,255,255) #   
strip.setPixelColorRGB(46,0,0,255) # Blue  
strip.setPixelColorRGB(47,255,255,255) #  
strip.setPixelColorRGB(48,0,0,255) # Blue  
strip.setPixelColorRGB(49,255,255,255) #  
strip.setPixelColorRGB(50,0,0,255) # Blue  
strip.setPixelColorRGB(51,255,255,255) #  
strip.setPixelColorRGB(52,0,0,255) # Blue  
strip.setPixelColorRGB(53,255,255,255) #  
strip.setPixelColorRGB(54,0,0,255) # Blue  
strip.setPixelColorRGB(55,255,255,255) #   
strip.setPixelColorRGB(56,0,0,255) # Blue  
strip.setPixelColorRGB(57,255,255,255) #   
strip.setPixelColorRGB(58,0,0,255) # Blue  
strip.setPixelColorRGB(59,255,255,255) #   
strip.setPixelColorRGB(60,0,0,255) # Blue
strip.setPixelColorRGB(61,255,255,255) #     
strip.setPixelColorRGB(62,0,0,255) # Blue
strip.setPixelColorRGB(63,255,255,255) #   
strip.setPixelColorRGB(64,0,0,255) # Blue  
strip.setPixelColorRGB(65,255,255,255) #   
strip.setPixelColorRGB(66,0,0,255) # Blue  
strip.setPixelColorRGB(67,255,255,255) #  
strip.setPixelColorRGB(68,0,0,255) # Blue  
strip.setPixelColorRGB(69,255,255,255) #  
strip.setPixelColorRGB(70,0,0,255) # Blue  
strip.setPixelColorRGB(71,255,255,255) # 
strip.setPixelColorRGB(72,0,0,255) # Blue  
strip.setPixelColorRGB(73,255,255,255) #   
strip.setPixelColorRGB(74,0,0,255) # Blue  
strip.setPixelColorRGB(75,255,255,255) #   
strip.setPixelColorRGB(76,0,0,255) # Blue  
strip.setPixelColorRGB(77,255,255,255) #  
strip.setPixelColorRGB(78,0,0,255) # Blue  
strip.setPixelColorRGB(79,255,255,255) #  
strip.setPixelColorRGB(80,0,0,255) # Blue  
strip.setPixelColorRGB(81,255,255,255) #  
strip.setPixelColorRGB(82,0,0,255) # Blue  
strip.setPixelColorRGB(83,255,255,255) #  
strip.setPixelColorRGB(84,0,0,255) # Blue  
strip.setPixelColorRGB(85,255,255,255) #   
strip.setPixelColorRGB(86,0,0,255) # Blue  
strip.setPixelColorRGB(87,255,255,255) #   
strip.setPixelColorRGB(88,0,0,255) # Blue  
strip.setPixelColorRGB(89,255,255,255) #   
strip.setPixelColorRGB(90,0,0,255) # Blue  
 

strip.show()