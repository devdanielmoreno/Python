'''
nif01.py
dni a nif
Dani Moreno
'''

dni = input("Introdueix el dni: ")
szNum = ''
for i in range(8):
    szNum += dni[i]
print("El NIF sense lletra és: %s"%szNum)
print("La lletra és: %s"%dni[8])
num = int(szNum)