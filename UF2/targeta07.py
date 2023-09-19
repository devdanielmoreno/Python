'''
targeta07.py

'''
import sys

N_TARGETA = 16

def bParse(sz):
    if len(sz)!=N_TARGETA:
      return False
    for c in sz:
        if not(c>='0' and c<='9'):
            return False
    return True
    
def cadena_a_llista(sz):
    l = []
    for c in sz:
        l.append(int(c))
    return l
"""
int nSumaUnitatDecimal(int n){
    return n/10+n%10;
}
"""
def nSumaUnitatDecimal(n):
     return n//10+n%10
     
nPesos=[2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1]
szT = input("Número tarjeta: ")
print("Heu introduit: \"%s\""%szT)
if bParse(szT):
    print("Comencem a analitzar la targeta ")
else:
    print("Targeta no correcta")
    sys.exit(1) #Sortida anormal del programa
nTargeta = cadena_a_llista(szT)
print(nTargeta)
nSumats = []
for i in range(N_TARGETA):
    print("%d x %d = %d "%(nTargeta[i],nPesos[i],nSumaUnitatDecimal(nTargeta[i]*nPesos[i])))
    nSumats.append(nSumaUnitatDecimal(nTargeta[i]*nPesos[i]))
print(nSumats)
sys.exit(0)