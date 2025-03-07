# LCD_scoreboard.py
# Written by: Brad Portouw
# Date: 3/6/25

# Testing a typical LCD screen setup for Arduino, with intent for it to show player score during a game.

# LCD screen used: https://www.digikey.com/en/products/detail/sunfounder/CN0295D/18668612?gclsrc=aw.ds&&utm_adgroup=&utm_source=google&utm_medium=cpc&utm_campaign=PMax%20Shopping_Product_Medium%20ROAS%20Categories&utm_term=&utm_content=&utm_id=go_cmp-20223376311_adg-_ad-__dev-c_ext-_prd-18668612_sig-CjwKCAiArKW-BhAzEiwAZhWsIAgvnu-1mc3klE2ltoby48NzVBuaIcExYII4619n62xK8gOBjT_hqBoCG3IQAvD_BwE&gad_source=1&gclid=CjwKCAiArKW-BhAzEiwAZhWsIAgvnu-1mc3klE2ltoby48NzVBuaIcExYII4619n62xK8gOBjT_hqBoCG3IQAvD_BwE
# Wiring diagram used: https://www.instructables.com/LCD-1602-With-Arduino-Uno-R3/

# *Note: the Arduino will require a firmata to be installed in order for this code to interface with it:
# LCD1602: https://github.com/primerobotics/Arduino/tree/master/LCD1602
# Utilize Arduino IDE to push above code to microcontroller

# import packages
import pyfirmata
import time
from pyfirmata import Arduino, util, STRING_DATA

board = pyfirmata.Arduino('COM3')

# Ideally the scoreboard of the pinball machine can change in real time to inputs made from switches, etc:
# Copying some code from the rollover switch test, with some real time inputs being shown on the board.

# Iterator which will loop to keep track of inputs and outputs
it = pyfirmata.util.Iterator(board)
it.start()

# pin 8 will check to see if the switch has closed.
switch = board.get_pin('d:3:i')
string = str(0)
# board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(string))

score = 0
while True:
    sw = switch.read()
    if sw is True:
        score = score + 10
        print(score)
        string = str(score)
        # board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(string))
        # sleep time seemingly is long enough that one rollover wont trigger multiple times.
        time.sleep(0.2)
    # Note on refresh rate, may need to be higher (check more than 10 times a second) depending upon how long the switch is closed for.
    time.sleep(0.1)