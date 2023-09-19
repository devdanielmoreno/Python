'''
yield00.py
20221202
'''
def usYield():
    for c in "Hola":
        yield c

def emprantYield():
    sz = ""
    for a in usYield():
        sz += a
    return sz

print("%s"%emprantYield())