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
        print("Caler negoci %d: %.2f€"%(n+1,fCalers[n]))
    return fS

N_NEGOCIS = 4
fCalers = []
fSuma = 0.;
for i in range(N_NEGOCIS):
    fNegoci = float(input("Caler negoci %d: "%(i+1)))
    fCalers.append(fNegoci)
'''
print("\nRecaptació per negoci:")
for i in range(N_NEGOCIS):
    print("Caler negoci %d: %.2f€"%(i+1,fCalers[i]))
    fSuma += fCalers[i]
'''
fSuma = fVisualitzaCalculaRecaptacio(fCalers)
print("\nRecaptació total: %.2f€"%fSuma)