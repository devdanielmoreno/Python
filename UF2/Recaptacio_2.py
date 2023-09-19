"""
eac02_funcllistes_01.py
20221124
"""
def fVisualitzaCalculaRecaptacio(fV):
    nQuants = len(fV)
    fS = 0.
    print("\nRecaptació per negoci:")
    for n in range(N_NEGOCIS):
        fS += fV[n]
        print("setmana %d: %.2f€"%(n+1,fCalers[n]))
    return fS

N_NEGOCIS = 5
fCalers = []
fSuma = 0.;
nom = (input("representant: "))
for i in range(N_NEGOCIS):
    fNegoci = float(input("setmana %d: "%(i+1)))
    fCalers.append(fNegoci)

fSuma = fVisualitzaCalculaRecaptacio(fCalers)
print("\nEl responsable %s ha recaptació total: %.2f€"%(nom,fSuma))