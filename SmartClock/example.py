import time
from neopixel import *
import argparse
from time import sleep

# LED strip configuration:


LED_COUNT      = 32      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


# Define functions which animate LEDs in various ways.
def color_set(strip, color):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()

def change_all_color(strip, color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)

def getRGB(r,g,b):
    return Color(g,r,b)

def set_stripcolor(weather_condition):
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()
    #color_set(strip, getRGB(0, 0, 0))
    if weather_condition==0:
        color_set(strip, getRGB(255, 0, 0)) # red(sunny)
    if weather_condition==1:
        color_set(strip, getRGB(125, 0, 255)) # green(cloudy)
    if weather_condition==2:
        color_set(strip, getRGB(0, 0, 255)) # blue(rainy)
    if weather_condition==3:
        color_set(strip, getRGB(255, 255, 255)) # white(snowy)


# Main program logic follows:
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args() 

   # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    
    
    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')
    
    while True:
        set_stripcolor(0)
        sleep(5)
        set_stripcolor(1)
        sleep(5)
        set_stripcolor(2)
        sleep(5)
        set_stripcolor(3)
        sleep(5) 


    #color_set(strip, getRGB(255,0,0))
    #time.sleep(3)
    #color_set(strip, getRGB(0,0,0))


