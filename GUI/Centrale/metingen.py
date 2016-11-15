import serial
import time
import collections
import random

def stuurcomando(poort, commando):
    print("poort:", poort, " commando:", commando)
#    def arduino(var):
        #light functie.
    if commando == 1:
        poort.write(bytes(b'%d') % commando)
        raw = poort.read(size=2)
        if raw:
            high,low = raw
            val = high * 256 + low
            val = 1023 - val
            return(val)
    #temperatuur functie.
    elif commando == 2:
        poort.write(bytes(b'%d') % commando)
        time.sleep(.1)
        s = int.from_bytes(poort.read(size=1), byteorder='big')
        val = round((float((s*5)/1024.0)-0.5)*100, 2) #berekening voor de temp value
        return(val)
    else:
        print("test")
        poort.write(bytes(b'%d') % commando)
        print("test2jwzboi")
        time.sleep(.1)
        val = int.from_bytes(poort.read(), byteorder='big')
        print(val)
        return val
#aoeoa
timer = 0
#lijstjes voor de licht
listlight = collections.deque(maxlen=60)
for j in range(60):
    waarde2 = random.randint(300, 800)
    listlight.append(waarde2)
listlightuur = collections.deque(maxlen=24)
listlightdag = collections.deque(maxlen=7)
listlightweek = collections.deque(maxlen=4)
listlightmaand = collections.deque(maxlen=12)
#lijstjes voor de temp
listtemp = collections.deque(maxlen=60)
for i in range(60):
    waarde = random.randint(18, 22)
    listtemp.append(waarde)
listtempuur = collections.deque(maxlen=24)
listtempdag = collections.deque(maxlen=7)
listtempweek = collections.deque(maxlen=4)
listtempmaand = collections.deque(maxlen=12)

def whileloop(poort):
    while True:
        global timer
        time.sleep(1)
        timer += 1
        if timer% 2 == 0:
            lightvalue = stuurcommando(poort ,1)
            print("lightval: ",lightvalue)
            tempvalue = stuurcommando(poort ,2)
            print("tempval: ",tempvalue)
            listtemp.append(tempvalue)
            listlight.append(lightvalue)
            #If statements voor de temperatuur
            if (len(listtemp) == 60):
                x = sum(listtemp) / 60
                listtempuur.append(x)
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
            #If statements voor licht
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
            print("listtemp: ",listtemp)
            print("listlight: ",listlight)

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
