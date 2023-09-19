'''
ex03.py
Dani Moreno Lao
20230110
'''

n = 0
while n >= 10 or n <= 20:  
    n = int(input("numero entre 10 i 20 (incluidos): "))
    if n >= 10 and n <= 20:
        print("Heu escrit %d"%n)
        break
