'''
factorial_00.py
Dani Moreno Lao
20221117
'''

def factorial (n):
    if n == 0:
        return 1
    return n * factorial(n-1)

nN = int(input("n: ")) #esto es normal
print("%d! = %d"%(nN,factorial(nN)))

for i in range(11):#esto es en bucle
    print("%d! = %d"%(i,factorial(i)))