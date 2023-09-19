"""
Dani Moreno Lao
20220929
ex 5

"""

i = float(input("i (en tant per 1): "))
n = float(input("Nombre de fraccionaments: "))
TAE = pow(1 + i/n,n)-1
print("TAE = %.4f en tant per 1"%(TAE))
print("TAE = %.2f %%"%(TAE*100))