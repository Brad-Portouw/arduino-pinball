# Derived from a tutorial from the website Real Python for interfacing Python with Arduino
# https://realpython.com/arduino-python/

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
board.digital[10].mode = pyfirmata.INPUT

# Infinite while loop to read the status of pin 10, and light up accordingly

while True:
    sw = board.digital[10].read()
    if sw is True:
        board.digital[13].write(1)
    else:
        board.digital[13].write(0)
    time.sleep(0.1)


