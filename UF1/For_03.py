"""
estRep13.py
Daniel Moreno Lao
20221108
"""
#nTaula = int(input("Taula de multiplicar: "))
for nTaula in range (1,6):
    print("Taula del %d: "%nTaula)
    for n in range (11):
        print("%d x %d\t= %d"%(n,nTaula,n*nTaula))
    print("----")
