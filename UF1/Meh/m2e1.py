'''

m2e1.py
Daniel Moreno
20221007

'''


cTipus = input("Tipus T,M,J o A?: ")
nEdat = int(input("Edat: "))
if cTipus == 'T' :
    print("pasa")
elif cTipus == 'M' and nEdat >= 13 :
    print("pasa")
elif cTipus == 'J' and nEdat >= 16 :
    print("pasa")
elif cTipus == 'A' and nEdat >= 18 :
    print("pasa")
else :
    print("no pasa")