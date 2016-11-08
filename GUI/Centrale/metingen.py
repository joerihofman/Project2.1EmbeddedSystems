import serial
import time

ser = serial.Serial (
    port='COM4',
    baudrate=19200,)

ser.isOpen()


#input = 1
while True:
    input2 = int(input("input graag: "))
    if input2 == 1:
        ser.write(bytes(b'%d') % input2)
        raw = ser.read(size=2)
        if raw:
            high,low = raw
            val = high * 256 + low
            val = 1023 - val
            print(val)
    else:
        ser.write(bytes(b'%d') % input2)
        time.sleep(.1)
        s = int.from_bytes(ser.read(),byteorder='big')
        print(s)


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