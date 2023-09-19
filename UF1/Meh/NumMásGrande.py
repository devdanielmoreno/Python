'''
05_enunciat.py
Daniel Moreno
20221006

'''
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
if a>=b and a>=c:
    print("El número %d és el més gran"%a)
elif b>=a and b>=c:
    print("El número %d és el més gran"%b)
else:
    print("El número %d és el més gran"%c)