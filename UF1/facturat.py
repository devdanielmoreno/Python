negoci = ['la sabateria','el taller de pneumátics','el supermercat','la gestoria']
Total=float(0)

for posicio in range (4):
    print("Introdueix els diners guanyats en",end="")
    DinersFacturats=float(input(negoci[posicio]+": "))
    Total+=DinersFacturats

print("El total facturat entre les 4 empreses es %.2f€"%(Total))