# Derived from a tutorial from the website Real Python for interfacing Python with Arduino
# https://realpython.com/arduino-python/

"""
Analog inputs are used to read voltages in a range rather than being on or off (1 or 0).
For instance the arduino can output 5 volts, but can read voltages between 0 and 5.
To read the analog voltage the arduino will attempt to convert the analog reading to digital by using a 10-bit
Analog to digital converter (ADC). With 1024 different voltage levels (2^10)
Resolution is lost between the bits, but 1024 different values should be sufficent for anything this Arduino hopes to accomplish

An analog output isn't entirely possible with an Arduino board, so pulse wave modulation (PWM) is uesed instead.
PWM is achieved by changing the duty cycle, or how long the output signal is set to high during a certain period.
Duty  cycle = fraction of time output is set to high.
By pulsing the high voltage (in this case 5v) a signal can be simiar to an analog signal because the power output does change.

* Only certain pins on the board are capable of PWM signals, which are signified by a ~
"""

# This test uses a potientiometer to vary an analog signal to the board, then uses a PWM pin to vary the brightness of an LED
# depending upon the analog reading.

# Import packages
import pyfirmata
import time

# Connect to the board through 'COM3"
board = pyfirmata.Arduino('COM3')

# Iterator which will loop to keep track of inputs and outputs
it = pyfirmata.util.Iterator(board)
it.start()

# Pin setup. Note the LED pin needs a p in the syntax for PWM
analog_input = board.get_pin('a:0:i')
led = board.get_pin('d:11:p')

# Blink the LED relative to the recieved analog voltage through the potentiometer
while True:
    analog_value = analog_input.read()
    if analog_value is not None:
        #Here pin 11 is capable of PWM, so the output will attempt to match the analog value.
        led.write(analog_value)
        time.sleep(0.1)
    else:
        time.sleep(0.1)
