nQN = int(input("Cantidad de numeros: "))
fNR = float(input("Numero real: "))
fInc = float(input("Increment real: "))
i=0
while (i<nQN):
    print("%.2f"%(fNR),end=" ")
    fNR += fInc
    i+=1