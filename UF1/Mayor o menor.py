"""
Dani Moreno Lao
20220930
    
"""

nom = input("Com et dius ?: ")
edat = int(input("Edat ?: "))
print("Hola %s, tens %d anys"%(nom, edat))   
if edat < 18:
    print("%s ets menor de edat"% nom)
else:
    print("%s ets mayor de edat"% nom)