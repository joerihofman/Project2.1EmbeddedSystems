from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#from tkinter.ttk import *
from GUI.Centrale import metingen
import matplotlib.pyplot as plt

class GUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.initUI()
        self.columnconfigure(10, weight=1)
        self.rowconfigure(3, weight=1)
#        self.curtab = None
#        self.tabs = {}
#        self.addtab()
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

def grafiek():
    values = [1,3]
    values2 = [8,3,5,7,2]
    plt.figure(1)
    plt.ion()
    plt.subplot(211)
    #plt.plot(metingen.testlist, 'r-')
    plt.plot(values, 'r-')
    plt.grid(True)
    plt.subplot(212)
    plt.plot(values2, 'r-')
    plt.grid(True)
    plt.show()

#TODO: opvulling weg halen
opvulling = 0

def main():
    def nieuwebordje():
        for i in range(metingen.aantalpoorten):
            a = i + 1
            nieuweframe = ttk.Frame(notebook, width=100, height=200)
            notebook.add(nieuweframe, text='Bord %d' % a)
            notebook.pack()
    root = Tk()
#    gui = GUI(root)
    root.geometry("600x450+300+300")
    notebook = ttk.Notebook(root)
    centraalframe = ttk.Frame(notebook, width=100, height=200)
    notebook.add(centraalframe, text='Centraal')
   # testknop = ttk.Button(centraalframe, text = "blabla v2", command=test)
    notebook.pack()
    testknop = ttk.Button(centraalframe, text = "grafiek", command=grafiek)
    testknop.place(x=10,y=10)
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
    centraalbordenaan = ttk.Label(centraalframe, text='Aantal borden aan: %d' % metingen.aantalpoorten)
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
    maxitemplabel = ttk.Label(centraalframe, text ='Maximale temperatuur: %d' % opvulling) #TODO: opvulling veranderen
    maxitemplabel.grid(row = 8, column = 0)
    maxirollabel = ttk.Label(centraalframe, text='Maximale uitrollengte: %d' % opvulling)
    maxirollabel.grid(row = 8, column = 2)
    maxitempbox = ttk.Combobox(centraalframe)
    maxitempbox.grid(row = 9, column =0)
    maxirolbox = ttk.Combobox(centraalframe)
    maxirolbox.grid(row = 9, column =2)
    whitespace4 = ttk.Label(centraalframe)
    whitespace4.grid(row=10,column=1)
    #TODO: leegmaken
    leegmakenknop = ttk.Button(centraalframe,text='Leegmaken')
    leegmakenknop.grid(row = 11, column = 0)
    #TODO: accepteren
    accepterenknop = ttk.Button(centraalframe,text='Accepteren')
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
    nieuwbordknop = ttk.Button(centraalframe,text = 'Nieuw bordje aansluiten',command=nieuwebordje)
    nieuwbordknop.grid(row=19,column=1)
    whitespace9 = ttk.Label(centraalframe)
    whitespace9.grid(row=20,column=1)
#    meting = Label(root,textvariable=test())
#    meting.place(x=100,y=50)
    #meting.pack()
#    gui.addtab()
    def callback():
        if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
            root.destroy()
            plt.close()
    root.protocol("WM_DELETE_WINDOW", callback)
    root.mainloop()


if __name__ == '__main__':
    main()


