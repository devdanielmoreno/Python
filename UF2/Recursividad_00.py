def suma(n):
    if n == 1:
        return 1
    else:
        return n + suma(n-1)

n = int(input("pon un numero: "))
print("La suma de %d es %d"%(n, suma(n)))

#este programa se suma a si mismo por ejemplo si pongo 10 va a sumar 10+9+8+7+6+5+4+3+2+1