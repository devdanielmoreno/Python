'''
m2e2.py
Dani Moreno
20221011

'''

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))
e = float(input("e: "))
f = float(input("f: "))
x=(e*d-b*f)/(a*d-b*c)
y=(a*f-e*c)/(a*d-b*c)
print("x = %.4f, y = %.4f"%(x,y))