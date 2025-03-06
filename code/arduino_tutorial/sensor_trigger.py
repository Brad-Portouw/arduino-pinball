# Derived from a tutorial from the website Real Python for interfacing Python with Arduino
# https://realpython.com/arduino-python/

# This code will look for a digital signal through a button, then will prompt a notification if the button is pressed

# Import packages
import pyfirmata
import time
import tkinter
from tkinter import messagebox

# Creating Tkinter's main window, then asking to hide it
root = tkinter.Tk()
root.withdraw()

# Connect to the board through 'COM3"
board = pyfirmata.Arduino('COM3')

# Iterator which will loop to keep track of inputs and outputs
it = pyfirmata.util.Iterator(board)
it.start()

# Pin Setup:
digital_input = board.get_pin('d:10:i')
led = board.get_pin('d:13:o')

while True:
    sw = digital_input.read()
    if sw is True:
        led.write(1)
        messagebox.showinfo("Notification", "Button was pressed")
        root.update()
        led.write(0)
    time.sleep(0.1)