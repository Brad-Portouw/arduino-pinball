# LCD1602_test.py
# Written by: Brad Portouw
# Date: 3/6/25

# Testing a typical LCD screen setup for Arduino, with intent for it to show player score during a game.

# LCD screen used: https://www.digikey.com/en/products/detail/sunfounder/CN0295D/18668612?gclsrc=aw.ds&&utm_adgroup=&utm_source=google&utm_medium=cpc&utm_campaign=PMax%20Shopping_Product_Medium%20ROAS%20Categories&utm_term=&utm_content=&utm_id=go_cmp-20223376311_adg-_ad-__dev-c_ext-_prd-18668612_sig-CjwKCAiArKW-BhAzEiwAZhWsIAgvnu-1mc3klE2ltoby48NzVBuaIcExYII4619n62xK8gOBjT_hqBoCG3IQAvD_BwE&gad_source=1&gclid=CjwKCAiArKW-BhAzEiwAZhWsIAgvnu-1mc3klE2ltoby48NzVBuaIcExYII4619n62xK8gOBjT_hqBoCG3IQAvD_BwE
# Wiring diagram used: https://www.instructables.com/LCD-1602-With-Arduino-Uno-R3/
# derived from YouTube tutorial: https://www.youtube.com/watch?v=c6RGNpAAHU8

# import packages
import pyfirmata
import time
from time import strftime
from pyfirmata import Arduino, util, STRING_DATA

board = pyfirmata.Arduino('COM3')

data = "Digital Clock"


while True:
    string=strftime('%I: %M : %S %p')
    board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(data))
    board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(string))
    time.sleep(1)
