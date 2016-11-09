"""
import serial
import serial.tools.list_ports
import sys
import time

ports = list(serial.tools.list_ports.comports())
for p in ports:
    comport = p[0][:5]

def checkport():
    try:
        global ports
        ser = serial.Serial(port=comport, baudrate=19200)
        global ser
    except serial.serialutil.SerialException:
        print("geen comport gevonden")

checkport()

ser.isOpen()
time.sleep(2)

def arduino(var):
    if var == 1:
        ser.write(bytes(b'%d') % var)
        raw = ser.read(size=2)
        if raw:
            high,low = raw
            val = high * 256 + low
            val = 1023 - val
            return val
    elif var == 2:
        ser.write(bytes(b'%d') % var)
        time.sleep(.1)
        s = int.from_bytes(ser.read(size=1), byteorder='big')
        s2 = s * 5
        s3 = float(s2 / 1024.0)
        val = (s3 - 0.5) * 100
        return(val)
    else:
        ser.write(bytes(b'%d') % var)
        time.sleep(.1)
        val = int.from_bytes(ser.read(),byteorder='big')
        return(val)

timer = 1

"""
testlist = [560, 585, 594, 594, 512, 658, 694, 865, 899, 927, 927, 918, 890, 890, 775, 668, 810, 764, 753, 902, 904, 932, 934, 934, 903, 852, 827, 741, 681, 685, 657, 631, 747, 840, 883, 830, 921, 908, 896, 868, 836, 596, 331, 291, 258, 218, 199, 189, 186, 183, 182, 214, 660, 615, 608, 439, 304, 261, 205, 238, 198, 201, 158, 164, 164, 166, 167, 170, 152, 183, 201, 200, 326, 762, 829, 833, 842, 846, 895, 919, 886, 914, 828, 665, 700, 657, 468, 353, 338, 409, 417, 395, 365, 375, 409, 663, 876, 932, 934, 934, 935, 935, 935, 936, 935, 935, 936, 936, 935, 935, 935, 935, 935, 936, 935, 935, 936]
"""
listlight = []
listtemp = []
while True:
    time.sleep(.1)
    timer += 1
    if timer% 3 == 0: #TODO verander dit naar 60 om elke 60 seconden waarden in een lijst te zetten.
        lightvalue = arduino(1)
        #tempvalue = arduino(2)
        listlight.append(lightvalue)
        #listtemp.append(tempvalue)
        timer = 0
        print(listlight)
        #print(listtemp)
        #if lightvalue < 500:
        #    arduino(4)

"""

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
#           pass
