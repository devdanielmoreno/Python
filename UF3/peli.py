import sys
import os

Pelis = {}

def vMenu():
    print()
    print("1) Llegeix arxiu")
    print("2) Quantes pel·lícules hi ha emmagatzemades?")
    print("3) Visualitza informació de totes les pel·lícules")
    print("4) Visualitza informació d'una pel·lícula")
    print("5) Esborra pel·lícula")
    print("6) Afegeix pel·lícula")
    print("7) Escriu arxiu")
    print("x) Surt")

def cQuinaOpcio():
    return input("Opció: ")

def bLlegeixArxiu():
    bR = False
    szF = input("Nom arxiu: ")
    try:
        f = open(szF,"r")
        bR = True
        f.close()
    except:
        bR = False
        
    return bR,szF

def vEscriuArxiu(szA):
    try:
        f = open(szA, "a")
        for i in Pelis.keys():
            if i == 'arxiu':
                continue
            for n in Pelis[i]:
                f.write("%s "%(n))
            f.write("\n")
        f.close()
        for i in Pelis.keys():
            if i == 'arxiu':
                continue
            del Pelis[i]
    except:
        print("\n")

def vAfegeixPelicula():
    tempTitol = input("Titol de la peli: ")
    tempDire = input("Director de la peli: ")
    tempProta = input("Protagonista de la peli: ")
    tempDur = int(input("Duració de la peli: "))
    Pelis[tempTitol] = tempTitol, tempDire, tempProta, tempDur
    return tempTitol

def ComptaPelis(szA):
    nComptador = 0
    f = open(szA, "r")
    szContingut = f.read()
    for c in szContingut:
        if c == "\n":
            nComptador+=1
    f.close()
    return nComptador

def visualitzaPelis(szA):
    f = open(szA, "r")
    szContingut = f.read()
    print(szContingut)
    f.close()

def bAExisteix():
    try:
        arxiu = Pelis["arxiu"]
        b = True
        return b, arxiu
    except:
        print("No s'ha pogut trobar el arxiu")
        arxiu = input("Introduïu el nom del arxiu: ")
        Pelis["arxiu"] = arxiu
        b = True
        return b, arxiu

def visualitzaUnaPeli(szA, nP):
    f = open(szA, "r")
    szContingut = f.read()
    nComptador = 0
    peli = ""
    for c in szContingut:
        if c == "\n":
            nComptador+=1
            continue
        if nComptador == nP-1:
            peli+=c
            if c == "\n":
                break
    print(peli)
    f.close()

def esborraPeli(szA, nP):
    f = open(szA, "r")
    fW = open("temp.txt", "w")
    szContingut = f.read()
    nComptador = 0
    for c in szContingut:
        if nComptador != nP-1:
            fW.write(c)
        if c == "\n":
            nComptador+=1
            continue
        if nComptador == nP-1:
            if c == "\n":
                break
    f.close()
    fW.close()
    f = open(szA, "w")
    fR = open("temp.txt", "r")
    f.write(fR.read())
    f.close()
    fR.close()
    os.remove("temp.txt")

def vPensa():
    b, arxiu = bAExisteix()
    if opt == '1':
        if b:
            print("L'arxiu %s existeix\n"%arxiu)
            if not Pelis["arxiu"]:
                Pelis["arxiu"] = arxiu
        else:
            print("L'arxiu %s no existeix\n"%arxiu)
    elif opt == '2':
        if b:
            nPelis = ComptaPelis(arxiu)
            print("%d" %nPelis)
        else:
            arxiu = input("Introduïu el nom del arxiu: ")
            nPelis = ComptaPelis(arxiu)
            print("Actualment hi ha %d pelicules" %nPelis)
    elif opt == '3':
        if b:
            visualitzaPelis(arxiu)
        else:
            arxiu = input("Introduïu el nom del arxiu: ")
            visualitzaPelis(arxiu)
    elif opt == '4':
        if b:
            numPeli = int(input("Quina peli vols visualitzar? "))
            visualitzaUnaPeli(arxiu, numPeli)
        else:
            numPeli = int(input("Quina peli vols visualitzar? "))
            arxiu = input("Introduïu el nom del arxiu: ")
            visualitzaUnaPeli(arxiu, numPeli)
    elif opt == '5':
        if b:
            numPeli = int(input("Quina peli vols esborrar? "))
            esborraPeli(arxiu, numPeli)
        else:
            numPeli = int(input("Quina peli vols esborrar? "))
            arxiu = input("Introduïu el nom del arxiu: ")
            esborraPeli(arxiu, numPeli)
    elif opt == '6':
        if b:
            vAfegeixPelicula()
        else:
            arxiu = input("Introduïu el nom del arxiu: ")
            vAfegeixPelicula()
    elif opt == '7':
        if b:
            vEscriuArxiu(arxiu)
        else:
            arxiu = input("Introduïu el nom del arxiu: ")
            vEscriuArxiu(arxiu)
    else:
        print("Manca de comprensió lectora")
    print("************************")
    return 0

while True:
    vMenu()
    opt = cQuinaOpcio()
    if opt == 'x' or opt == 'X':
        print("Heu escollit sortir")
        sys.exit()
    vPensa()