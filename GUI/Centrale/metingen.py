import serial
import time


ser = serial.Serial('COM7',19200)
while True:
    try:
        ser = serial.Serial('COM7',19200)
    except:
        print("geen com gevonden")


def read_arduino():
    time.sleep(0.01)
    x = ser.read()
    x = x + ser.read()
    print(x)


while 1 == 1:
    read_arduino()