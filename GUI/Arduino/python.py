import serial
import serial.tools.list_ports

class Arduino:
    arduinos = {}
    ardcount = 0

    @classmethod
    def get(cls, nr):
        if cls.arduinos[nr]:
            return cls.arduinos[nr]
        else:
            return None

    @classmethod
    def scan(cls):
        portsdict = {}
        print("portsdict: ", portsdict)
        nieuw = []
        print("nieuw: ", nieuw)
        portlist = list(serial.tools.list_ports.comports())
        for p in portlist:
            portsdict[portlist.index(p)] = str(p)
            print("portsdict2", portsdict)
        for key,value in portsdict.items():
            port = portsdict[key]
            strip = port[0:4]
            print("strip: ", strip)
            for k,v in Arduino.arduinos:
                if v == (strip):
                    print("niks gevonden")
                    pass
                else:
                    nieuw.append(strip)
                    print("iets gevonden")
            for v in nieuw:
                Arduino.arduinos[Arduino.ardcount] = Arduino(Arduino.ardcount, strip)
                nieuw.append(Arduino.arduinos[Arduino.ardcount])
                Arduino.ardcount+=1

    def __init__(self, nummer, poort):
        self.nummer = nummer
        self.poort = poort
        self.serial = serial.Serial(port=poort, baudrate=19200)
        print(self.nummer)
        print(self.poort)

    def commandosturen(self, commando):
        pass





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