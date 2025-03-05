# Derived from a tutorial from the website Real Python for interfacing Python with Arduino
# https://realpython.com/arduino-python/

#Code will cause the onboard led 13 to blink to check if the code was recieved

# Importing packages:
import pyfirmata
import time

board = pyfirmata.Arduino('COM3')

while True:
    board.digital[13].write(1)
    time.sleep(1)
    board.digital[13].write(0)
    time.sleep(1)

