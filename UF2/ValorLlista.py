def nValorMaximLlista(nLlista):
    nMaxim = nLlista[0]

    for element in nLlista:
        if element > nMaxim:
            nMaxim = element
    return nMaxim



nVectorA = [25,34,12,-3,7,15,36,56,42,30]
nVectorB = [250,340,120,-30,70,150,360,560,420,300]

print("Valor maxim de la llista %d"%nValorMaximLlista(nVectorA))
print("Valor maxim de la llista %d"%nValorMaximLlista(nVectorB))