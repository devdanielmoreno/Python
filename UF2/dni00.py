'''
dni00.py
Dani Moreno
'''
lletresDni = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
dni = int(input("dni: "))
print("%d-%c"%(dni,lletresDni[dni%23]))