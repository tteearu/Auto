# import Raspberry Pi GPIO support into Python environment
import RPi.GPIO as GPIO
# import a sleep function from time module
from time import sleep

led = 10, 22, 27  # GPIO number where the led is connected

# Tell the GPIO module to use GPIO numbering used by processor
GPIO.setmode(GPIO.BCM)

# Set GPIO no 18 to output mode
GPIO.setup(led, GPIO.OUT)

# Blink some leds
while True:
    GPIO.output(led, False)
    sleep(0.5)  # Sleep for 1 second
    GPIO.output(led, True)
    sleep(0.5)
