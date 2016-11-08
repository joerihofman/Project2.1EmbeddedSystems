import serial
import time


while True:
    try:
        ser = serial.Serial('COM7',19200)
        def read_arduino():
            time.sleep(0.01)
            x = ser.read()
            x = x + ser.read()
            print(x)
    except:
        print("geen com gevonden")
        def read_arduino():
            None
        break





#while 1 == 1:
#    read_arduino()