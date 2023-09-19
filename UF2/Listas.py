llista = ["Dani","Moreno"]
for el in llista:
    #print(el)
    print("+++++")
    for lletra in el:
        print(lletra)
    print("-----")
llista[0] = "Pep"
llista[1] = "Garcia"
for el in llista:
    print(el)
print("**")
llista += ["i", "Martínez"]
for el in llista:
    print(el)