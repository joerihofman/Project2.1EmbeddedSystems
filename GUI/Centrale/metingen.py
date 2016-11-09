import serial
import time

ser = serial.Serial (
    port='COM4',
    baudrate=19200,)
ser.isOpen()
time.sleep(3)

def arduino(var):
    val=0
    if var == 1:
        ser.write(bytes(b'%d') % var)
        raw = ser.read(size=2)
        if raw:
            high,low = raw
            val = high * 256 + low
            val = 1023 - val
            return val
    else:
        ser.write(bytes(b'%d') % var)
        time.sleep(.1)
        val = int.from_bytes(ser.read(),byteorder='big')
        return(val)

light = 1
while True:
    time.sleep(0.5)
    light += 1
    if light % 5 == 0:
        lightvalue = arduino(1)
        light = 0
        if lightvalue < 500:
            arduino(4)



                    # while True:
#     try:
#         ser = serial.Serial('COM3',19200)
#     except:
#         print("geen com gevonden")
#
# def read_arduino(input):
#     ser.write(bytes(b'%d')%input)
#     time.sleep(.1)
#     print(ser.read())
#
# input2 = int(input("Kies commando: "))
#
# read_arduino(input2)