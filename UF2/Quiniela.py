import random

nColumnes = int(input("Cuantas columnas quieres: "))
nlista = [1,2,"x"]

for i in range(15):
    for i in range(nColumnes):
        print("!" + str(random.choice(nlista)) + "!",end="")
    print()