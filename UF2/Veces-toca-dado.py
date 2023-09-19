import random

def nDau():
    return random.randint(1,6)

llista = []
for i in range(1000):
    # print("%d "%(nDau()+nDau()),end="")
    llista.append(nDau() + nDau())
nSuma9 = 0
nSuma10 = 0
for i in range(1000):
    if llista[i] == 9:
        nSuma9 += 1
    if llista[i] == 10:
        nSuma10 += 1
print("%d cops a donat nou la suma dels dos daus. I suma deu %d cops"%(nSuma9,nSuma10))