'''
yield01.py 
20221202
'''
def ventall_caracters(c1,c2):
   for c in range(ord(c1),ord(c2)+1):
       yield chr(c)

def vOmple(cInicial,cFinal):
    szRetorn = ""
    for c in ventall_caracters(cInicial,cFinal):
        szRetorn += c
    return szRetorn

print("%s"%vOmple("a","f"))

for a in "ABCDEF":
    print("%s"%a,end = "")
print()