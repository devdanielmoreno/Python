szNom = input("Com et dius ?: ")
nEdat = int(input("Edat ?: "))
print("Hola %s, tens %d anys"%(szNom, nEdat))   
if nEdat < 18:
    print("%s ets menor de edat"% szNom)
else:
    print("%s ets mayor de edat"% szNom)