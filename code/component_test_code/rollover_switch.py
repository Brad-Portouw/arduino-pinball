# rollover_switch.py
# Written by: Brad Portouw
# Date: 3/6/25

# Code to interface with an Arduino Uno to read the triggering of a rollover switch, a common switch that is used in pinball machines.
# Assumption with the switch is that it will work in a normally-open contact (NO)
# Switch used:
# https://www.betsonparts.com/amusement-redemption/sub-mini-switch-db5-style.html

# Typically there are many switches being used in the pinball machine at one time, but only one pinball.
# This may mean that the switches can be run in parallel all being connected to one pin because they should only be triggered one at a time.
#
# Import packages
import pyfirmata
import time

# Connect to the board through 'COM3"
board = pyfirmata.Arduino('COM3')

# Iterator which will loop to keep track of inputs and outputs
it = pyfirmata.util.Iterator(board)
it.start()

# pin 10 will check to see if the switch has closed, while pin 13 will light a LED to show the switch closing.
switch_input = board.get_pin('d:10:i')
LED = board.get_pin('d:13:o')

score = 0
while True:
    switch = switch_input.read()
    if switch is True:
        LED.write(1)
        score = score + 10
        print(score)
        # sleep time seemingly is long enough that one rollover wont trigger multiple times.
        time.sleep(0.2)
    else:
        LED.write(0)
    # Note on refresh rate, may need to be higher (check more than 10 times a second) depending upon how long the switch is closed for.
    time.sleep(0.1)



