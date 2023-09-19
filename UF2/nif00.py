'''
nif00.py
dni a nif
Dani Moreno
'''
def bParse(sz):
    if len(sz) != 8:
        return False
    for c in sz:
        if not(c >= '0' and c <= '9'):
            return False
        return True

dni = input("Introdueix el numero del dni: ")
if bParse(dni):
    residu = int(dni)%23
    llista = "TRWAGMYFPDXBNJZSOVHLCKE"
    print("%s-%s"%(dni,llista[residu]))
else:
    print("%s no és un número de DNI vàlid."%dni)
