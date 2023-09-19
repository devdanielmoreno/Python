"""
Dani Moreno Lao
20220930
ex 7    
"""
import math

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

disc=b*b-4*a*c
x1=(-b+math.sqrt(disc))/(2*a)
x2=(-b-math.sqrt(disc))/(2*a)
print("x1: %f, x2: %f"%(x1,x2))

