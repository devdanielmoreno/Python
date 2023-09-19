'''
m2e6.py
Dani Moreno
20221018

'''
nSegonsInicials = int(input("Nombre de segons: "))
nSegonsFinals = nSegonsInicials % 60
print("%ds"%nSegonsFinals)
nMinutsInicials = nSegonsInicials// 60
nMinutsFinals = nMinutsInicials% 60
print("%dm"%nMinutsFinals)
nHoresInicials = nMinutsFinals// 60
nHoresFinals = nHoresInicials% 24
print("%dh"%nHoresFinals)
nDiesInicials = nHoresInicials// 30
nDiesFinals = nDiesInicials % 30
print("%dd"%nDiesInicials)
print("%d dies, %d hores, %d minuts i %d segons"%
                (nDiesInicials,nHoresFinals,nMinutsFinals,nSegonsFinals))