sNom = input("Hola com et dius?: ")
sCurs = input("A quin curs perstanys?: ")
fSuma = 0.0
for i in range(5):
    fNota = float(input("Nota %d: "%(i+1)))
    fSuma += fNota/5
print("Hola %s de %s la teva mitjana de programació és: %.2f"%(sNom,sCurs,fSuma))