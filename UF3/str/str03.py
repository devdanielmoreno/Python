'''
str03.py
20230414
'''
szCognomA = "Pérez"
szCognomB = " Rodríguez"
szText = input("Introduïu un text: ")
# print("El text \"%s\" té %d caràcters"%(szText, len(szText)))  
print('El text "%s" té %d caràcters'%(szText, len(szText))) 
szText = szText + " " + szCognomA + szCognomB
print('El text "%s" té %d caràcters'%(szText, len(szText))) 