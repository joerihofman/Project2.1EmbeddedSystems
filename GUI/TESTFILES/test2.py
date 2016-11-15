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