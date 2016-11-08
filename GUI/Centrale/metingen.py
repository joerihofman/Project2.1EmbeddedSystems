import serial
import time

ser = serial.Serial (
    port='COM3',
    baudrate=19200,)

ser.isOpen()

#input = 1
while True:
    input2 = input("input graag: ")
    # als je niets invuld stopttdt het
    if input2 > 0 and input2 <= 9:
        if input2 == 1:
            input3 = num(input2)
            ser.write(bytes(b'%d') % input3)
            raw = ser.read(size=2)
            if raw:
                high,low = raw
                val = high * 256 + low
                val = 1023 - val
                print(val)
        else:
            input3 = num(input2)
            ser.write(bytes(b'%d') % input3)
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

#def num(t):
#     try:
#         return int(t)
#     except ValueError:
#         pass