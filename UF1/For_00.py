'''
estrep03_01.py
Dani Moreno
20221025
'''
num=int(input("n: "))
nR = 1
for n in range(num):
    # print("%d"%(n+1),end = " ")
    nR = nR * (n+1) # o nR  *= n+1
print("%d! = %d"%(num,nR))