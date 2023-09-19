nQN = int(input("Cantidad de numeros: "))
fNR = float(input("Numero real: "))
fInc = float(input("Increment real: "))

for i in range(nQN):
    print("%.2f"%(fNR),end=" ")
    fNR += fInc