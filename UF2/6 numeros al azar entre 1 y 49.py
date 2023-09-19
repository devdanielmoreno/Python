'''
Dani Moreno Lao
20221108
'''
import random

for i in range(5):
    n1 = random.randint(1,49)
    n2 = random.randint(1,49)
    while n1 == n2 :
        n2 = random.randint(1,49)
    n3 = random.randint(1,49)
    while n1 == n3 or n2 == n3:
        n3 = random.randint(1,49)
    n4 = random.randint (1,49)
    while n1 == n4 or n2 == n4 or n3 == n4:
        n4 = random.randint (1,49)
    n5 = random.randint (1,49)
    while n1 == n5 or n2 == n5 or n3 == n5 or n4 == n5:
        n5 = random.randint (1,49)
    while n1 == n5 or n2 == n5 or n3 == n5 or n4 == n5:
        n5 = random.randint (1,49)
    n6 = random.randint (1,49)
    while n1 == n6 or n2 == n6 or n3 == n6 or n4 == n6 or n5 == n6:
        n6 = random.randint (1,49)
    print("%d %d %d %d %d %d"%(n1,n2,n3,n4,n5,n6))