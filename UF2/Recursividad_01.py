'''
m4e2_01.py
Dani Moreno Lao
20221118
'''
def pot(b,e):
    if e == 0:
        return 1
    return b*pot(b,e-1)

def n1s(n):
    if n == 0 or n == 1:
        return n
    return 10 *n1s(n-1)+1

for i in range(1,9):
    print(pot(n1s(i),2))