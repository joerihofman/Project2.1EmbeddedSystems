from tkinter import *
from tkinter import messagebox
from tkinter import ttk


import matplotlib.pyplot as plt

from GUI.Arduino import python
from GUI.Centrale import metingen

root = Tk()
notebook = ttk.Notebook(root)
notebook = ttk.Frame(notebook, width = 100, height = 200)
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