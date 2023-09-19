import random

num = random.randint(1,100)
intentos = 0
n1 = 0
while num != n1:
    n1 = int(input("Hola pon un numero del 1 al 100: "))
    if num < n1:
        print("Pon un num más pequeño")
    elif num > n1:
        print("Pon un num más grande")
    intentos+=1
print("El numero %d es correcte Has hacertat en %d intents"%(num,intentos))