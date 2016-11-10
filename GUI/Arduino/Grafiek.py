import matplotlib.pyplot as pl

values = [1, 3, 5, 3, 2, 8] #dit zijn test waarden
pl.plot(values, 'r-', label='values')
pl.show()

#for loop tot 60
 #   stop dat in nieuwe lijst, lijst van uren.
listtemp = []
listtempuur = []
listtempdag = []
listtempweek = []
listtempmaand = []
#for i in range(0,60):
if (len(listtemp) == 60):
    x = sum(listtemp) / 60
    listtempuur.append(x)
    del listtemp[:]

if(len(listtempuur) == 24):
    y = sum(listtempuur) / 24
    listtempdag.append(y)
    del listtempuur[:]

if(len(listtempdag) == 7):
    h = sum(listtempdag) / 7
    listtempweek.append(h)
    del listtempdag[:]

if(len(listtempweek) == 4):
    z = sum(listtempdag) / 4
    listtempmaand.append(z)
    del listtempweek[:]

if(len(listtempmaand) == 12):
    del listtempmaand[:]
