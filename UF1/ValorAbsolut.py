'''
m2e7.py
funcion 3
Dani Moreno Lao
20221018
'''

def lfValorAbsolut(lf):
    if lf < 0:
        lf = lf * -1
    return lf

x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))
x3 = float(input("x3: "))
y3 = float(input("y3: "))

fA = 0.5*((x1-x2)*(y3-y2)-(y1-y2)*(x3-x2))
print("Area: %.4f"%fA)