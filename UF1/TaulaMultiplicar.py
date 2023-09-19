from lib2to3.pgen2.token import NOTEQUAL

nTaula = int(input("Taula de multiplicar: "))
n = 0
while n <= 10:
    print("%d x %d \t= %d"%(nTaula,n,nTaula*n))
    n+= 1