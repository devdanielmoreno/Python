# targeta08.py

import sys

N_TARGETA = 16

def bParse(szT):
    if len(szT) != N_TARGETA:
        return False
    for c in szT:
        if not(c >= '0' and c <= '9'):
            return False
    return True

def cadena_a_llista(sz):
    l = []
    for c in sz:
        l.append(int(c))
    return l

def nSumaUnitatDecimal(n):
    return (n // 10) + (n % 10)  # La divisió amb // serveix per fer una divisió entera.

def llistaSumats(nT, nP):
    nS = []
    for i in range(N_TARGETA):
        # print("%d x %d = %d" % (nT[i], nP[i], nSumaUnitatDecimal(nT[i] * nP[i])))
        nS.append(nSumaUnitatDecimal(nT[i] * nP[i]))  # Fem una llista de nSumats.
    return nS

def nSumaTotal(nLlistaT):
    nSuma = 0
    for n in nLlistaT:
        nSuma += n
    return nSuma

nPesos = [2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1]

szT = input("Número tarjeta: ")
print("Heu introduit: \"%s\"" % szT)

if bParse(szT):
    print("Comencem a analitzar la targeta ")
else:
    print("Targeta no correcta.")
    sys.exit(1)  # Sortida anormal del programa.

nTargeta = cadena_a_llista(szT)
print("nTargeta: ", nTargeta)

nSumats = llistaSumats(nTargeta, nPesos)
print("nPesos:   ", nPesos)
print("nSumats:  ", nSumats)
print("nSuma:  ", nSumaTotal(nSumats))

if nSumaTotal(nSumats) % 10 == 0:
    print("%s és vàlida" % szT)
else:
    print("%s no és vàlida" % szT)

sys.exit(0)  # Actua com un return 0.