import sys

if len(sys.argv) == 2:
    nomFitxer = sys.argv[1]
else:
    nomFitxer = input("Nom arxiu: ")
try:
    f = open(nomFitxer)
    print("%s existeix"%nomFitxer)
    print("El contingut de l'arxiu és: ")
    szContingut = f.read()
    nL = 1
    szLinia = ""
    for c in szContingut:
        #print("%d) %s"%(nL, linia))
        #nL+=1
        if c != "\n":
            szLinia += c
        else:
            print("%d) %s"%(nL, szLinia))
            nL+=1
            szLinia = ""
except:
    print("%s no existeix"%nomFitxer)