from tkinter import *
from tkinter import ttk
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
x = ""
def test():
#    global x
    try:
#        invoer = int(input('Commando? '))
#        x = metingen.read_arduino(commando)
#        print(x)
#        return x
        print("aaa")
#        return x
    except:
        x = "except"
        print(x)
        return x
#aa
def grafiek():
    #values = [1,2,5,3,8,2,6,4,5,6,7,1,2,5,3,6,4,3,7]
    values2 = [8,3,5,7,2]
    fig = plt.figure()
#    a = fig.addsubplot(111)
#    a = plt.plot(metingen.testlist, 'r-')

    b = plt.plot(values2, 'r-')
    plt.grid(True)
    plt.show()



#aa`
def main():
    def nieuwetabbladen():
        for i in range(8):
            nieuweframe = ttk.Frame(notebook, width=100, height=200)
            notebook.add(nieuweframe, text='frame %d' % i)
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
    sep1 = ttk.Separator(centraalframe, orient="horizontal")
    sep1.grid(row = 2, column = 1, sticky= 'ew')
    sep2 = ttk.Separator(centraalframe, orient="horizontal")
    sep2.grid(row=2, column=2, sticky='ew')
    sep3 = ttk.Separator(centraalframe, orient="horizontal")
    sep3.grid(row=2, column=0, sticky='ew')
    centraalbordenaan = ttk.Label(centraalframe,text='Aantal borden aan: %d' % metingen.aantalpoorten)
    centraalbordenaan.grid(row = 3, column = 1)
    sep4 = ttk.Separator(centraalframe, orient="horizontal")
    sep4.grid(row = 4, column = 1, sticky= 'ew')
    sep5 = ttk.Separator(centraalframe, orient="horizontal")
    sep5.grid(row=4, column=2, sticky='ew')
    sep6 = ttk.Separator(centraalframe, orient="horizontal")
    sep6.grid(row=4, column=0, sticky='ew')
    maxitemplabel = ttk.Label(centraalframe, text ='Maximale temperatuur:')
    maxitemplabel.grid(row = 5, column = 0)
    maxirollabel = ttk.Label(centraalframe, text='Maximale uitrollengte:')
    maxirollabel.grid(row = 5, column = 2)
    maxitempbox = ttk.Combobox(centraalframe)
    maxitempbox.grid(row = 6, column =0)
    maxirolbox = ttk.Combobox(centraalframe)
    maxirolbox.grid(row = 6, column =2)
    leegmakenknop = ttk.Button(centraalframe,text='Leegmaken WIP')
    leegmakenknop.grid(row = 7, column = 0)
    accepterenknop = ttk.Button(centraalframe,text='Accepteren WIP')
    accepterenknop.grid(row=7,column=2)
    sep7 = ttk.Separator(centraalframe, orient="horizontal")
    sep7.grid(row=8, column=0, sticky='ew')
    sep8 = ttk.Separator(centraalframe, orient="horizontal")
    sep8.grid(row=8, column=1, sticky='ew')
    sep9 = ttk.Separator(centraalframe, orient="horizontal")
    sep9.grid(row=8, column=2, sticky='ew')
    openknop = ttk.Button(centraalframe,text='Alle luiken open WIP')
    openknop.grid(row=9, column=0)
    sluitknop = ttk.Button(centraalframe,text='Alle luiken sluiten WIP')
    sluitknop.grid(row=9,column=2)
    sep10 = ttk.Separator(centraalframe, orient="horizontal")
    sep10.grid(row=10,column=0,sticky='ew')
    sep11 = ttk.Separator(centraalframe, orient="horizontal")
    sep11.grid(row=10, column=1,sticky='ew')
    sep12 = ttk.Separator(centraalframe, orient="horizontal")
    sep12.grid(row=10, column=2,sticky='ew')
    nieuwbordknop = ttk.Button(centraalframe,text = 'Nieuw bordje aansluiten WIP')
    nieuwbordknop.grid(row=11,column=1)
#    meting = Label(root,textvariable=test())
#    meting.place(x=100,y=50)
    #meting.pack()
#    gui.addtab()
    root.mainloop()


if __name__ == '__main__':
    main()


#def addTab(knopnaam):
#    knopnaam = ttk.Frame(notebook)


    #self.scherm = Tk()
    #self.scherm.mainloop()


#    def mainloop(self):
#        self.scherm.mainloop()

"""

    def addtab(self):
        tabslen = len(self.tabs)
        if tabslen < 10:
            tab = {}
            btn_central = Button(self, text="centrale", command=lambda: self.raiseTab(0))
            btn_central.grid(row=0, column=0, sticky=W+E)
            btn_arduinos = Button(self, text="Tab "+str(tabslen), command=lambda: self.raiseTab(tabslen))
            btn_arduinos.grid(row=0, column=tabslen, sticky=W+E)

            textbox = Text(self.parent)
            textbox.grid(row=1, column=0, columnspan=10, rowspan=2, sticky=W+E+N+S, in_=self)

            # Y axis scroll bar
            scrollby = Scrollbar(self, command=textbox.yview)
            scrollby.grid(row=7, column=5, rowspan=2, columnspan=1, sticky=N+S+E)
            textbox['yscrollcommand'] = scrollby.set

            tab['id']=tabslen
            tab['btn_arduinos']=btn_arduinos
            tab['txtbx']=textbox
            self.tabs[tabslen] = tab
            self.raiseTab(tabslen)

    def raiseTab(self, tabid):
        g("cur_tab"+str(self.curtab))
        if self.curtab!= None and self.curtab != tabid and len(self.tabs)>1:
                self.tabs[tabid]['txtbx'].lift(self)
                self.tabs[self.curtab]['txtbx'].lower(self)
        self.curtab = tabid
"""