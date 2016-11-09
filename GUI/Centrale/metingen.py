import serial
import serial.tools.list_ports
import time

ports = list(serial.tools.list_ports.comports())
for p in ports:
    comport = p[0][:5]
    print(p)

aantalpoorten = len(ports)

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
            return(val)
    elif var == 2:
        ser.write(bytes(b'%d') % var)
        time.sleep(.1)
        s = int.from_bytes(ser.read(size=1), byteorder='big')
        val = round((float((s*5)/1024.0)-0.5)*100,2) #berekening voor de temp value
        return(val)
    else:
        ser.write(bytes(b'%d') % var)
        time.sleep(.1)
        val = int.from_bytes(ser.read(),byteorder='big')
        return(val)

timer = 0
listlight = []
listtemp = []
def whileloop():
    while True:
        global timer
        time.sleep(1)
        timer += 1
        if timer% 2 == 0: #TODO verander dit naar 60 om elke 60 seconden waarden in een lijst te zetten.
            lightvalue = arduino(1)
            tempvalue = arduino(2)
            listlight.append(lightvalue)
            listtemp.append(tempvalue)
            timer = 0
            print(listlight)
            print(listtemp)
            #if lightvalue < 500:
            #    arduino(4)


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
