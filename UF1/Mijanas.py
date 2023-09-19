'''
m2e5.py
Dani Moreno
20221013
'''

def doble(a):
    return 2 * a
def mitjana(x,y,z):
    m = (x+y+z)/3
    return m
def mitjag(x,y,z):
    return pow(x*y*z,1./3)
def var(x,y,z):
    return mitjana(x*x,y*y,z*z)-(mitjana(x,y,z)*mitjana(x,y,z))
def dt(x,y,z):
    return pow(var(x,y,z),1./2)

n = float(input("n: "))
print("el doble de %.4f és %.4f"%(n,doble(n)))
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
print("la mitjana aritmetica de %.2f, %.2f i %.2f és %.3f"%(a,b,c,mitjana(a,b,c)))
print("la mitjana geometrica de %.2f, %.2f i %.2f és %.3f"%(a,b,c,mitjag(a,b,c)))
print("la variança de %.2f, %.2f i %.2f és %.3f"%(a,b,c,var(a,b,c)))
print("la desviació típica de %.2f, %.2f i %.2f és %.3f"%(a,b,c,dt(a,b,c)))