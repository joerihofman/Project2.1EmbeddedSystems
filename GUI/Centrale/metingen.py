import serial
import time


ser = serial.Serial('COM3',19200)
while True:
    try:
        ser = serial.Serial('COM3',19200)
    except:
        print("geen com gevonden")


def read_arduino(input):
    ser.write(bytes(b'%d')%input)
    print(ser.read())
    time.sleep(.1)