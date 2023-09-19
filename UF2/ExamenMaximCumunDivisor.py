'''
Examen
ASIX
MaximComunDivisor
'''
def nMaximComuDiv(u,v):
    t = 0
    if u < 0:
        u = -1 * u
    if v < 0:
        v = -1 * v
    while(v != 0):
        t = u
        u = v
        v = t%v
    return u



a = int(input("a: "))
b = int(input("b: "))
print("MCD( %d, %d ) = %d"%(a,b,nMaximComuDiv(a,b)))