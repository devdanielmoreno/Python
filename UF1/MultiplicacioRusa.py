def multiplicacioRussa(a, b):
    suma = 0

    while a > 0:
        if a%2 == 1:
            suma = suma + b
        a = a//2 # // part entera
        b = b*2
    return suma
    
x = int(input("x: "))
y = int(input("y: "))
print("%d x %d = %d"%(x, y, multiplicacioRussa(x, y)))