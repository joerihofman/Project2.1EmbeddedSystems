import serial
import serial.tools.list_ports
import time

ports = list(serial.tools.list_ports.comports())
for p in ports:
    comport = p[0][:5]

aantalpoorten = len(ports)

if ports:
    def checkport():
        try:
            global comport
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
    #lijstjes voor de licht
    listlight = []
    listlightuur = []
    listlightdag = []
    listlightweek = []
    listlightmaand = []
    #lijstjes voor de temp
    listtemp = []
    listtempuur = []
    listtempdag = []
    listtempweek = []
    listtempmaand = []
    def whileloop():
        while True:
            global timer
            time.sleep(1)
            timer += 1
            if timer% 2 == 0: #TODO verander dit naar 60 om elke 60 seconden waarden in een lijst te zetten.
                lightvalue = arduino(1)
                tempvalue = arduino(2)
                listtemp.append(tempvalue)
                listlight.append(lightvalue)
                #If statements voor de temperatuur
                if (len(listtemp) == 60):
                    x = sum(listtemp) / 60
                    listtempuur.append(x)
                    del listtemp[:]
                if (len(listtempuur) == 24):
                    y = sum(listtempuur) / 24
                    listtempdag.append(y)
                    del listtempuur[:]
                if (len(listtempdag) == 7):
                    h = sum(listtempdag) / 7
                    listtempweek.append(h)
                    del listtempdag[:]
                if (len(listtempweek) == 4):
                    z = sum(listtempdag) / 4
                    listtempmaand.append(z)
                    del listtempweek[:]
                if (len(listtempmaand) == 12):
                    del listtempmaand[:]

                #If statements voor de licht
                if (len(listlight) == 60):
                    x = sum(listlight) / 60
                    listlightuur.append(x)
                    del listlight[:]
                if (len(listlightuur) == 24):
                    y = sum(listlightuur) / 24
                    listlightdag.append(y)
                    del listlightuur[:]
                if (len(listlightdag) == 7):
                    h = sum(listlightdag) / 7
                    listlightweek.append(h)
                    del listlightdag[:]
                if (len(listlightweek) == 4):
                    z = sum(listlightdag) / 4
                    listlightmaand.append(z)
                    del listlightweek[:]
                if (len(listlightmaand) == 12):
                    del listlightmaand[:]
                #listtemp.append(tempvalue)
                timer = 0
                #print(listlight)
                #print(listtemp)
                #if lightvalue < 500:
                #    arduino(4)
else:
    pass

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
