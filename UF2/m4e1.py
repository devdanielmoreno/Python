'''
m4e1.py
Dani Moreno Lao
20221117
'''


def pot(base,exponent):
    if exponent == 0:
        return 1
    return base * pot(base,exponent-1)

b=2.
for i in range(11):
    print("%.2f ^ %d = %.2f"%(b,i,pot(b,i)))