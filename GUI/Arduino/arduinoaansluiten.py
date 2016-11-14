"""
import serial
import serial.tools.list_ports

ports = list(serial.tools.list_ports.comports())
print("lees nieuwe poort1")
portsdict = {}
for p in ports:
    portsdict[ports.index(p)] = str(p)

for key in portsdict:
    poort = portsdict[key]
    poortstrip = poort[0:4]
    print(poortstrip)

aantalpoorten = len(ports)

#if ports:
def checkport():
    try:
        poortstrip
    except NameError:
        print("geen comports")
    else:
        ser = serial.Serial(port=poortstrip, baudrate=19200)
        print(ser)
        global ser

def checkport():
    if poortstrip:
        ser = serial.Serial(port=poortstrip, baudrate=19200)
        print(ser)
        global ser
    else:
        print("geen comports")
"""
#checkport()
