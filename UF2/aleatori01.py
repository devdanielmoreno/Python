'''
aleatori01.py
Daniel Moreno Lao
20221104
'''
import random

def nValorAleatori(nMin, nMax):
    return random.randint(nMin, nMax)

for i in range(51):
    print("%d "%nValorAleatori(23,26), end="")
print("\n")