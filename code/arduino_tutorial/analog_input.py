# Derived from a tutorial from the website Real Python for interfacing Python with Arduino
# https://realpython.com/arduino-python/

"""
Analog inputs are used to read voltages in a range rather than being on or off (1 or 0).
For instance the arduino can output 5 volts, but can read voltages between 0 and 5.
To read the analog voltage the arduino will attempt to convert the analog reading to digital by using a 10-bit
Analog to digital converter (ADC). With 1024 different voltage levels (2^10)
Resolution is lost between the bits, but 1024 different values should be sufficent for anything this Arduino hopes to accomplish
"""

# Import packages
import pyfirmata
import time

# Connect to the board through 'COM3"
board = pyfirmata.Arduino('COM3')

# Iterator which will loop to keep track of inputs and outputs
it = pyfirmata.util.Iterator(board)
it.start()

analog_input = board.get_pin('a:0:i')
led = board.get_pin('d:13:o')

# Blink the LED relative to the recieved analog voltage through the potentiometer
while True:
    analog_value = analog_input.read()
    if analog_value is not None:
        delay = analog_value + 0.01
        led.write(1)
        time.sleep(delay)
        led.write(0)
        time.sleep(delay)
    else:
        time.sleep(0.1)

