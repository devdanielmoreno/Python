import sys

if len(sys.argv) == 2:
    nomFitxer = sys.argv[1]
else:
    nomFitxer = input("Nom arxiu: ")
try:
    f = open(nomFitxer)
    print("%s existeix"%nomFitxer)
    print("El contingut de l'arxiu és: ")
    print(f.read())
except:
    print("%s no existeix"%nomFitxer)