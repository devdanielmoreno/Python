'''
str05.py
20230414
'''
CONTRASENYA = "pA55w0rD"
szContrasenya = "pA55w0rD"
szContrasenya2 = "pA55w0rd"

if szContrasenya == CONTRASENYA:
    print("%s és el mateix que %s"%(szContrasenya,CONTRASENYA))
else:
    print("%s no és el mateix que %s"%(szContrasenya,CONTRASENYA))
    
if szContrasenya2 == CONTRASENYA:
    print("%s és el mateix que %s"%(szContrasenya2,CONTRASENYA))
else:
    print("%s no és el mateix que %s"%(szContrasenya2,CONTRASENYA))