from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import matplotlib.pyplot as plt

from GUI.Arduino import python
from GUI.Centrale import metingen
from GUI.Centrale import nieuwbordje


class GUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.initUI()
        self.columnconfigure(10, weight=1)
        self.rowconfigure(3, weight=1)
        self.pack(fill=BOTH, expand=1, padx=5, pady=5)

    def initUI(self):
        self.parent.title("Test")
        self.pack(fill=BOTH, expand=1)

def test():
    try:
        try1 = "try"
        print(try1)
        return try1
    except:
        try1="except"
        print(try1)
        return try1

def grafiekuur():
    plt.figure(1)
    plt.suptitle("Temperatuur/licht per minuut over een uur")
    plt.subplot(211)
    plt.plot(metingen.listtemp, 'r-')
    plt.xlabel("Minuut")
    plt.ylabel("Temperatuur")
    plt.grid(True)
    plt.subplot(212)
    plt.plot(metingen.listlight, 'r-')
    plt.xlabel("Minuut")
    plt.ylabel("Licht")
    plt.grid(True)
    plt.show()

def grafiekdag():
    plt.figure(1)
    plt.suptitle("Temperatuur/licht per uur over een dag")
    plt.subplot(211)
    plt.plot(metingen.listtempuur, 'r-')
    plt.xlabel("Uur")
    plt.ylabel("Temperatuur")
    plt.grid(True)
    plt.subplot(212)
    plt.plot(metingen.listlightuur, 'r-')
    plt.xlabel("Uur")
    plt.ylabel("Licht")
    plt.grid(True)
    plt.show()

def grafiekweek():
    plt.figure(1)
    plt.suptitle("Temperatuur/licht per dag over een week")
    plt.subplot(211)
    plt.plot(metingen.listtempdag, 'r-')
    plt.xlabel("Dag")
    plt.ylabel("Temperatuur")
    plt.grid(True)
    plt.subplot(212)
    plt.plot(metingen.listlightdag, 'r-')
    plt.xlabel("Dag")
    plt.ylabel("Licht")
    plt.grid(True)
    plt.show()

def grafiekmaand():
    plt.figure(1)
    plt.suptitle("Temperatuur/licht per week over een maand")
    plt.subplot(211)
    plt.plot(metingen.listtempweek, 'r-')
    plt.xlabel("Week")
    plt.ylabel("Temperatuur")
    plt.grid(True)
    plt.subplot(212)
    plt.plot(metingen.listlightweek, 'r-')
    plt.xlabel("Week")
    plt.ylabel("Licht")
    plt.grid(True)
    plt.show()

def grafiekjaar():
    plt.figure(1)
    plt.suptitle("Temperatuur/licht per maand over een jaar")
    plt.subplot(211)
    plt.plot(metingen.listtempmaand, 'r-')
    plt.xlabel("Maand")
    plt.ylabel("Temperatuur")
    plt.grid(True)
    plt.subplot(212)
    plt.plot(metingen.listlightmaand, 'r-')
    plt.xlabel("Maand")
    plt.ylabel("Licht")
    plt.grid(True)
    plt.show()

#TODO: opvulling weg halen
opvulling = 0

def main():
    instellingenvenster_dict={}

    #maakt een instellingenvenster aan voor een bordje
    def instellingenvenster(nummer):
        instellingenvenstertje = Tk()
        instellingenvenster_dict.update({nummer : instellingenvenstertje})
        instellingenvenstertje.geometry("300x200+300+300")
        ivensterlabel = ttk.Label(instellingenvenstertje, text='Instellingen bord %d' % nummer)
        ivensterlabel.grid(row=0,column=1)
        isep1 = ttk.Separator(instellingenvenstertje)
        isep1.grid(row=1,column=0,sticky='ew')
        isep2 = ttk.Separator(instellingenvenstertje)
        isep2.grid(row=1,column=1,sticky='ew')
        isep3 = ttk.Separator(instellingenvenstertje)
        isep3.grid(row=1,column=2,stick='ew')
        iwhitespace1 = ttk.Label(instellingenvenstertje)
        iwhitespace1.grid(row=2,column=1)
        iuitrollengte = ttk.Label(instellingenvenstertje, text='Uitrollengte: ')
        iuitrollengte.grid(row=3,column=1)
        #TODO: laat knoppen de uitrollengte van het bord instellen
        i50cm = ttk.Button(instellingenvenstertje, text='50 cm')
        i50cm.grid(row=4,column=0)
        i100cm = ttk.Button(instellingenvenstertje, text='100 cm')
        i100cm.grid(row=4,column=1)
        ihelemaal= ttk.Button(instellingenvenstertje, text='Helemaal')
        ihelemaal.grid(row=4,column=2)

        def isluit():

            del instellingenvenster_dict[nummer]
            instellingenvenstertje.destroy()
        instellingenvenstertje.protocol("WM_DELETE_WINDOW", isluit)
    #maakt een tabblad aan voor een bordje

#    def nieuwebordje():
        #todo: laat maar een tabblad per bord open kunnen laten gaan
#        nieuwbordjetab()
#        metingen.leesnieuweport()

    def nieuwbordjetab():
        arduino = python.Arduino.scan()
#        for i in range(len(python.Arduino.arduinos)):
#            welkearduino = python.Arduino.arduinos[i]
        for i in python.Arduino.arduinos:
            welkearduino = python.Arduino.get(i).poort
            a = i + 1
            nieuweframe = ttk.Frame(notebook, width=100, height=200)
            notebook.add(nieuweframe, text='Bord %d' % a)
            notebook.pack()
            bordlabel = ttk.Label(nieuweframe, text='Bord %d' % a)
            bordlabel.grid(row=0,column=0)
            bordsep1 = ttk.Separator(nieuweframe,orient="horizontal")
            bordsep1.grid(row=1,column=0,sticky='ew')
            bordsep2 = ttk.Separator(nieuweframe, orient="horizontal")
            bordsep2.grid(row=1, column=1, sticky='ew')
            bordsep3 = ttk.Separator(nieuweframe, orient="horizontal")
            bordsep3.grid(row=1, column=2, sticky='ew')
            borduitgeroldlabel1 = ttk.Label(nieuweframe, text ='Uitgerold:')
            borduitgeroldlabel1.grid(row=2,column=1)
            #TODO: geef door of bord is uitgerold of niet
            borduitgeroldlabel2 = ttk.Label(nieuweframe, text ='Ja/Nee')
            borduitgeroldlabel2.grid(row=3,column=1)
            bordwhitespace1= ttk.Label(nieuweframe)
            bordwhitespace1.grid(row=4,column=1)
            bordgrafieklabel= ttk.Label(nieuweframe, text ='Grafiek')
            bordgrafieklabel.grid(row=5,column=1)
            #TODO: laat knoppen grafieken openen
            uurknop= ttk.Button(nieuweframe,text='Uur', command = grafiekuur)
            uurknop.grid(row=6,column=0)
            dagknop= ttk.Button(nieuweframe,text='Dag', command = grafiekdag)
            dagknop.grid(row=6,column=1)
            weekknop= ttk.Button(nieuweframe,text='Week', command = grafiekweek)
            weekknop.grid(row=6,column=2)
            maandknop= ttk.Button(nieuweframe,text='Maand', command = grafiekmaand)
            maandknop.grid(row=7,column=0)
            jaarknop= ttk.Button(nieuweframe, text='Jaar', command = grafiekjaar)
            jaarknop.grid(row=7,column=1)
            bordwhitespace2 = ttk.Label(nieuweframe)
            bordwhitespace2.grid(row=8,column=1)
            bordsep4 = ttk.Separator(nieuweframe, orient="horizontal")
            bordsep4.grid(row=9,column=0,sticky='ew')
            bordsep5 = ttk.Separator(nieuweframe, orient="horizontal")
            bordsep5.grid(row=9, column=1,sticky='ew')
            bordsep6 = ttk.Separator(nieuweframe, orient="horizontal")
            bordsep6.grid(row=9, column=2,sticky='ew')
            #TODO: laat knoppen het bord in- en uitrollen
            inrolknop = ttk.Button(nieuweframe, text='Inrollen')
            inrolknop.grid(row=10,column=0)
            uitrolknop = ttk.Button(nieuweframe,text='Uitrollen')
            uitrolknop.grid(row=10,column=2)
            bordsep7 = ttk.Separator(nieuweframe, orient="horizontal")
            bordsep7.grid(row=11, column=0, sticky='ew')
            bordsep8 = ttk.Separator(nieuweframe, orient="horizontal")
            bordsep8.grid(row=11, column=1, sticky='ew')
            bordsep9 = ttk.Separator(nieuweframe, orient="horizontal")
            bordsep9.grid(row=11, column=2, sticky='ew')
            instellingenbordknop = ttk.Button(nieuweframe,text='Instellingen Bordje',command=lambda: instellingvensterenknop())
            instellingenbordknop.grid(row=12,column=1)
            bordwhitespace3 = ttk.Label(nieuweframe)
            bordwhitespace3.grid(row=13,column=1)
            sluitknop = ttk.Button(nieuweframe,text='Sluit tabblad',command=nieuweframe.destroy)
            sluitknop.grid(row=14,column=2)
            welkearduinoisdit = ttk.Label(nieuweframe, text="ard:{} ".format(welkearduino))
            welkearduinoisdit.grid(row=16, column=2)

            #TODO: als bordjes aangesloten zijn aan tabbladen knop weer aan kunnen zetten
            def instellingvensterenknop():
                instellingenvenster(a)
                instellingenbordknop.state(["disabled"])


    root = Tk()

    maxrol= 150
    maxtemp= 25

    def setmaxtemp(waarde):
        main.maxtemp = waarde

    root.geometry("600x450+300+300")
    notebook = ttk.Notebook(root)
    centraalframe = ttk.Frame(notebook, width=100, height=200)
    notebook.add(centraalframe, text='Centraal')
    notebook.pack()
    #Grafiekknop = ttk.Button(centraalframe, text = "grafiek", command=grafiekminuut)
    #Grafiekknop.place(x=10,y=10)
    centraallabel = ttk.Label(centraalframe,text= 'Centraal')
    centraallabel.grid(row = 1, column = 1 )
    whitespace1 = ttk.Label(centraalframe)
    whitespace1.grid(row = 2, column = 1)
    sep1 = ttk.Separator(centraalframe, orient="horizontal")
    sep1.grid(row = 3, column = 1, sticky= 'ew')
    sep2 = ttk.Separator(centraalframe, orient="horizontal")
    sep2.grid(row=3, column=2, sticky='ew')
    sep3 = ttk.Separator(centraalframe, orient="horizontal")
    sep3.grid(row=3, column=0, sticky='ew')
    centraalbordenaan = ttk.Label(centraalframe, text='Aantal borden aan: %d' % python.Arduino.ardcount)
    centraalbordenaan.grid(row=4, column=1)
    whitespace2 = ttk.Label(centraalframe)
    whitespace2.grid(row=5,column=1)
    sep4 = ttk.Separator(centraalframe, orient="horizontal")
    sep4.grid(row = 6, column = 1, sticky= 'ew')
    sep5 = ttk.Separator(centraalframe, orient="horizontal")
    sep5.grid(row=6, column=2, sticky='ew')
    sep6 = ttk.Separator(centraalframe, orient="horizontal")
    sep6.grid(row=6, column=0, sticky='ew')
    whitespace3 = ttk.Label(centraalframe)
    whitespace3.grid(row=7,column=1)
    maxitemplabel = ttk.Label(centraalframe, text ='Maximale temperatuur(°C): %d' % opvulling) #TODO: opvulling veranderen
    maxitemplabel.grid(row = 8, column = 0)
    maxirollabel = ttk.Label(centraalframe, text='Maximale uitrollengte(CM): %d' % opvulling)
    maxirollabel.grid(row = 8, column = 2)
    maxitempbox = Entry(centraalframe)
    maxitempbox.grid(row = 9, column =0)
    maxirolbox = OptionMenu(centraalframe, maxrol, 50, 100, 150)
    maxirolbox.grid(row = 9, column =2)
    whitespace4 = ttk.Label(centraalframe)
    whitespace4.grid(row=10,column=1)
    leegmakenknop = ttk.Button(centraalframe,text='Leegmaken',command=lambda:maxitempbox.set(''))
    leegmakenknop.grid(row = 11, column = 0)
    #TODO: accepteren
    accepterenknop = ttk.Button(centraalframe,text='Accepteren',command = setmaxtemp(maxitempbox.get()))
    accepterenknop.grid(row=11,column=2)
    whitespace5 = ttk.Label(centraalframe)
    whitespace5.grid(row=12,column=1)
    sep7 = ttk.Separator(centraalframe, orient="horizontal")
    sep7.grid(row=13, column=0, sticky='ew')
    sep8 = ttk.Separator(centraalframe, orient="horizontal")
    sep8.grid(row=13, column=1, sticky='ew')
    sep9 = ttk.Separator(centraalframe, orient="horizontal")
    sep9.grid(row=13, column=2, sticky='ew')
    whitespace6 = ttk.Label(centraalframe)
    whitespace6.grid(row=14,column=1)
    #TODO: Alle luiken open
    openknop = ttk.Button(centraalframe,text='Alle luiken open')
    openknop.grid(row=15, column=0)
    #TODO: Alle luiken sluiten
    sluitknop = ttk.Button(centraalframe,text='Alle luiken sluiten')
    sluitknop.grid(row=15,column=2)
    whitespace7 = ttk.Label(centraalframe)
    whitespace7.grid(row=16,column=1)
    sep10 = ttk.Separator(centraalframe, orient="horizontal")
    sep10.grid(row=17,column=0,sticky='ew')
    sep11 = ttk.Separator(centraalframe, orient="horizontal")
    sep11.grid(row=17, column=1,sticky='ew')
    sep12 = ttk.Separator(centraalframe, orient="horizontal")
    sep12.grid(row=17, column=2,sticky='ew')
    whitespace8 = ttk.Label(centraalframe)
    whitespace8.grid(row=18,column=1)
    #TODO: Nieuw bordje aansluiten
    nieuwbordknop = ttk.Button(centraalframe,text = 'Nieuw bordje aansluiten',command=nieuwbordjetab)
    nieuwbordknop.grid(row=19,column=1)
    whitespace9 = ttk.Label(centraalframe)
    whitespace9.grid(row=20,column=1)
#    meting = Label(root,textvariable=test())
#    meting.place(x=100,y=50)
#    meting.pack()
#    gui.addtab()
    def vraag():
        if messagebox.askokcancel("Stoppen", "Weet je zeker dat je wilt stoppen?"):
            root.destroy()
            for k,v in instellingenvenster_dict.items():

                v.destroy()
            plt.close()
    root.protocol("WM_DELETE_WINDOW", vraag)
    root.mainloop()


if __name__ == '__main__':
    main()


