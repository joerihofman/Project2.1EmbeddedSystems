from pyserial.serial import serialwin32
import time


ser = serialwin32.Serial('COM7',19200)


def read_arduino():
    time.sleep(0.01)
    x = ser.read()
    x = x + ser.read()
    print(x)


while 1 == 1:
    read_arduino()