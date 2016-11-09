from tkinter import *
from tkinter import ttk
#from tkinter.ttk import *
from GUI.Centrale import metingen
#import matplotlib.pyplot as plt

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


#aa`
def main():
    def eenheleboeltestknoppen():
        for i in range(5):
            nieuweframe = ttk.Frame(notebook, width=100, height=200)
            notebook.add(nieuweframe, text=i)
            notebook.pack()
    root = Tk()
    values = [1, 3, 5, 3, 2, 8]
#    gui = GUI(root)
    root.geometry("600x450+300+300")
    notebook = ttk.Notebook(root)
    testframe1 = ttk.Frame(notebook, width=100, height=200)
    testframe2 = ttk.Frame(notebook, width=500, height=100)
    notebook.add(testframe1, text='frame 1')
    notebook.add(testframe2, text='frame 2')
    testknop = ttk.Button(testframe1, text = "blabla v2", command=test)
#    plt.plot(values, 'r-')
#    plt.show()
    notebook.pack()
    testknop = ttk.Button(testframe1, text = "blabla v2", command=test)
    testknop.place(x=10,y=10)
    knop=ttk.Label(testframe1, textvariable=x)
    knop.place(x=10,y=35)
    knop.pack()
    testknop2 = ttk.Button(testframe1, text = "nieuw tabblad", command =eenheleboeltestknoppen)
    testknop2.place(x=10,y=60)
    testknop2.pack()

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