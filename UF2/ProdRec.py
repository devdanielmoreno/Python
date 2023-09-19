def nProdRec(n):
    if n >= 2:
        return n * nProdRec(n - 1)
    return n

nNum = int(input("Numero: "))
print("nProdRec(%d) = %d" %(nNum, nProdRec(nNum)))
