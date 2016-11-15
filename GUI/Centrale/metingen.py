from GUI.Arduino import arduinoaansluiten
import serial
import time
import collections

def stuurcomando(poort, commando):
    print("poort:", poort, " commando:", commando)
#    def arduino(var):
        #light functie.
    if commando == 1:
        poort.serial.write(bytes(b'%d') % commando)
        raw = poort.serial.read(size=2)
        if raw:
            high,low = raw
            val = high * 256 + low
            val = 1023 - val
            return(val)
    #temperatuur functie.
    elif commando == 2:
        poort.serial.write(bytes(b'%d') % commando)
        time.sleep(.1)
        s = int.from_bytes(poort.serial.read(size=1), byteorder='big')
        val = round((float((s*5)/1024.0)-0.5)*100,2) #berekening voor de temp value
        return(val)
    else:
        print("test")
        poort.serial.write(bytes(b'%d') % commando)
        time.sleep(.1)
        val = int.from_bytes(poort.serial.read(),byteorder='big')
        return(val)

    timer = 0
    #lijstjes voor de licht
    listlight = collections.deque(maxlen=60)
    listlightuur = collections.deque(maxlen=24)
    listlightdag = collections.deque(maxlen=7)
    listlightweek = collections.deque(maxlen=4)
    listlightmaand = collections.deque(maxlen=12)
    #lijstjes voor de temp
    listtemp = collections.deque(maxlen=60)
    listtempuur = collections.deque(maxlen=24)
    listtempdag = collections.deque(maxlen=7)
    listtempweek = collections.deque(maxlen=4)
    listtempmaand = collections.deque(maxlen=12)

    def whileloop():
        while True:
            global timer
            time.sleep(1)
            timer += 1
            if timer% 60 == 0:
                lightvalue = arduino(1)
                tempvalue = arduino(2)
                listtemp.append(tempvalue)
                listlight.append(lightvalue)
                #If statements voor de temperatuur
                if (len(listtemp) == 60):
                    x = sum(listtemp) / 60
                    listtempuur.append(x)
                    #voor %60 begin je opnieuw, de restwaarde moet de index,positie in lijst, geven van de lijst
                    #waar op die positie de meting wordt vervangen
                    # 68 % 60 = 8 > index = 8
                    # 119 % 60 = 59 > index = 59
                if (len(listtempuur) == 24):
                    y = sum(listtempuur) / 24
                    listtempdag.append(y)
                if (len(listtempdag) == 7):
                    h = sum(listtempdag) / 7
                    listtempweek.append(h)
                if (len(listtempweek) == 4):
                    z = sum(listtempdag) / 4
                    listtempmaand.append(z)
                if (len(listtempmaand) == 12):
                    del listtempmaand[:]
                #If statements voor de licht
                if (len(listlight) == 60):
                    a = sum(listlight) / 60
                    listlightuur.append(a)
                if (len(listlightuur) == 24):
                    b = sum(listlightuur) / 24
                    listlightdag.append(b)
                if (len(listlightdag) == 7):
                    c = sum(listlightdag) / 7
                    listlightweek.append(c)
                if (len(listlightweek) == 4):
                    d = sum(listlightdag) / 4
                    listlightmaand.append(d)
                if (len(listlightmaand) == 12):
                    del listlightmaand[:]
                #listtemp.append(tempvalue)
                timer = 0

                #print(listlight)
                #print(listtemp)
                #if lightvalue < 500:
                #    arduino(4)
#else:
#    pass

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
