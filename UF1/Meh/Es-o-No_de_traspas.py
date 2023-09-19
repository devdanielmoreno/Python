'''
06_enunciat.py
Daniel Moreno
20221007

'''

nAny = int(input("Any:"))
if nAny % 4 == 0:
    if nAny % 100 == 0:
        if nAny % 400 == 0:
            print("L'any %d es de traspas"%nAny)
        else:
            print("L'any %d no es de traspas"%nAny)
    else:
        print("L'any %d no es de traspas"%nAny)
else:
    print("L'any %d no es de traspas"%nAny)