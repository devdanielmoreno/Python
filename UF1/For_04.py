"""
estRep14.py
Dani Moreno Lao
20221108
"""
n = int(input("n: "))
bEsPrimer = True
for i in range(2,n):
    if n %i == 0:
        bEsPrimer = False
        break
if bEsPrimer:
    print("%d es primer"% n)
else:
    print("%d no es primer"% n)
    