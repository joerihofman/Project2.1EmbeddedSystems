import serial
import time

ser = serial.Serial (
    port='COM3',
    baudrate=19200,)
ser.isOpen()
time.sleep(3)


def arduino(var):
    # light functie.
    if var == 1:
        ser.write(bytes(b'%d') % var)
        raw = ser.read(size=2)
        if raw:
            high, low = raw
            val = high * 256 + low
            val = 1023 - val
            return (val)
    # temperatuur functie.
    elif var == 2:
        ser.write(bytes(b'%d') % var)
        time.sleep(.1)
        s = int.from_bytes(ser.read(size=1), byteorder='big')
        val = round((float((s * 5) / 1024.0) - 0.5) * 100, 2)  # berekening voor de temp value
        return (val)
    else:
        ser.write(bytes(b'%d') % var)
        time.sleep(.1)
        val = int.from_bytes(ser.read(), byteorder='big')
        return (val)

light = 1
while True:
    time.sleep(.1)
    light += 1
    if light%2==0:
        val = int(input('voer wat in'))
        lightvalue = arduino(val)
        light=0
        print(lightvalue)


