import serial
import sys
import time

ser = serial.Serial (
    port='COM3',
    baudrate=19200,)

ser.isOpen()
print("1:licht  2:temp  3:up    4:down  5:status    6:ping  7:uitrol5   8:uitrol10  9:uitrol15")
#input = 1
def invoercommando():
    while True:
        try:
            input2 = int(input("input graag: "))
            # als je niets invuld stopttdt het
            if input2 > 0 and input2 <= 9:
                if input2 == 1:
                    ser.write(bytes(b'%d') % input2)
                    raw = ser.read(size=2)
                    if raw:
                        high,low = raw
                        val = high * 256 + low
                        val = 1023 - val
                        print(val)
                if input2 == 2:
                    ser.write(bytes(b'%d') % input2)
                    time.sleep(.1)
                    s = int.from_bytes(ser.read(size=1),byteorder='big')
                    s2 = s*5
                    s3 = float(s2/1024.0)
                    s4 = (s3-0.5)*100
                    print(s4)
                else:
                    ser.write(bytes(b'%d') % input2)
                    time.sleep(.1)
                    s = int.from_bytes(ser.read(),byteorder='big')
                    print(s)
        except ValueError:
            print("probeer een getal")
            invoercommando()
        except:
            print("er ging iets goed fout")
            sys.exit()


invoercommando()

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