import neopixel
np = neopixel.NeoPixel(machine.Pin(18), 150)


np[0] = (255, 0, 0) # set to red, full brightness
np[1] = (0, 128, 0) # set to green, half brightness
np[2] = (0, 0, 64)  # set to blue, quarter brightness
 
np.write()