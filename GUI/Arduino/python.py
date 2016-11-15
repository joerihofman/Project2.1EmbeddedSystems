import serial
import serial.tools.list_ports
import time
from GUI.Centrale import metingen

class Arduino:
    arduinos = {}
    ardcount = 0

    @classmethod
    def get(cls, nr):
        if cls.arduinos[nr]:
            return cls.arduinos.get(nr)
        else:
            return None

    @classmethod
    def scan(cls):
        print(Arduino.arduinos)
        portsdict = {}
        print("portsdict: ", portsdict)
        nieuw = []
        print("nieuw: ", nieuw)
        portlist = list(serial.tools.list_ports.comports())
        print("portlist: ",portlist)
        for p in portlist:
            portsdict[portlist.index(p)] = str(p)
            print("portsdict", portsdict)
        for k,v in portsdict.items():
            print("k, v:",k,",",v)
            port = portsdict[k]
            portstrip = port[0:4]
            print("strp",str(portstrip))
            print("arduino items: ",Arduino.arduinos.items())
            if portstrip == Arduino.arduinos.items():
                print("niks gevonden")
                pass
            else:
                print("iets gevonden")
                nieuw.append(str(portstrip))
                print("NIEUW IN k,v", nieuw)
#            a = nieuw[0]
#            print(a)
#            print(type(a))
        for i in nieuw:
            print(i)
#            a = nieuw.index(i)
#            print("a", a)
#                print("b", b)
#                for key,val in portsdict.items():
#                    portstr = portsdict[key]
#            x = 0
            Arduino.arduinos[Arduino.ardcount] = Arduino(Arduino.ardcount, i)
#            Arduino(Arduino.ardcount, port)
            Arduino.ardcount+=1
        print("nieuw: ",nieuw)
        nieuw.clear()
        print("arduino's: ",Arduino.arduinos)

    def __init__(self, nummer, poort):
        self.nummer = nummer
        self.poort = poort
        self.serials = serial.Serial(port=self.poort[0:4], baudrate=19200)
        self.serials.isOpen()
        print(self.nummer)
        print(self.poort)
        print(self.serials)
#        Arduino.arduinos[nummer] = (poort)

    def commandosturen(self, commando):
        metingen.stuurcomando(Arduino.arduinos.get(self.nummer), commando)

    def openserial(self):
        print("het is gelukt denk ik",self.serials, self.nummer)
#        self.serial = serial.Serial(port=self.poort[0:4], baudrate=19200)
#        self.serial.open()
#        time.sleep(2)





#    def x(self):
#        ser = serial.Serial(port=self.poort, baudrate=19200)
#        print(ser)
#        return ser

#    portsdictlen = len(arduinolist)
"""
def poort():
    for key in Arduino.portsdict:
        port = Arduino.portsdict[key]
        poortstrip = port[0:4]
        arduinolist.append(poortstrip)
        print(arduinolist)
#        yield poortstrip
"""
#def printdict():
#    print(Arduino.portsdict)

    # portlist = list(serial.tools.list_ports.comports())
    # portsdict = {}
    # for p in portlist:
    #     portsdict[portlist.index(p)] = str(p)
    # for key in portsdict:
    #     poort = portsdict[key]
    #     poortstrip = poort[0:4]
    #     print(poortstrip)
#def main():
#    try:
#        Arduino.poort
#    except NameError:
#        print("geen arduino gevonden")
#    else:

#        def poort(self):
#            pass


#def aantal(self):
#    return Arduino.ardcount

#if __name__ == '__main__':
#    main()


"""
for p in portlist:
    portsdict[portlist.index(p)] = str(p)
    print("portsdict", portsdict)
for key,value in portsdict.items():
    port = portsdict[key]
#            print("port", port)
    strip = port[0:4]
    print("strip: ", strip)
#            values = [v for k,v in Arduino.arduinos.items() if value in v]
    for k,v in portsdict.items():
#                for ka, va in Arduino.arduinos.items():
        if v in Arduino.arduinos:
            print("niks gevonden")
            pass
        else:
            nieuw.append(strip)
            print("iets gevonden")
        for i in nieuw:
            Arduino.arduinos[Arduino.ardcount] = Arduino(Arduino.ardcount, strip)
            nieuw.append(Arduino.arduinos[Arduino.ardcount])
            Arduino.ardcount+=1
"""
