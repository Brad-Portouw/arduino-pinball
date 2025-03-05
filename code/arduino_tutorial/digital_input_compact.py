# Derived from a tutorial from the website Real Python for interfacing Python with Arduino
# https://realpython.com/arduino-python/

# This is a recreation of 'digital_input.py' but with more compact syntax by pyfirmata
# Code is meant to read digital inputs to pin 10, then show it was recieved by lighting up pin 13

# Import packages
import pyfirmata
import time

# Connect to the board through 'COM3"
board = pyfirmata.Arduino('COM3')

# Iterator which will loop to keep track of inputs and outputs
it = pyfirmata.util.Iterator(board)
it.start()

# Set pin 10 as a digital input pin. default pin setting is output
# Set pin 13 as a digital ouptut pin.
#syntax is:
# 1. the type of pin (a for analog or d for digital)
# 2. the number of the pin
# 3. the mode of the pin (i for input o for output)
digital_input = board.get_pin('d:10:i')
led = board.get_pin('d:13:o')


# Infinite while loop to read the status of pin 10, and light up accordingly

while True:
    sw = digital_input.read()
    if sw is True:
        led.write(1)
    else:
        led.write(0)
    time.sleep(0.1)
