nomFitxer = input("Nom arxiu: ")
try:
    f = open(nomFitxer)
    print("%s existeix"%nomFitxer)
except:
    print("%s no existeix"%nomFitxer)