'''
m2e4.py
Dani Moreno
20221013
'''

a = float(input("a: "))
b = float(input("b: "))
r = float(input("r: "))
x = float(input("x: "))
y = float(input("y: "))

if (x-a)*(x-a)+(y-b)*(y-b) <= r*r:
    print("dins")
else:
    print("fora")