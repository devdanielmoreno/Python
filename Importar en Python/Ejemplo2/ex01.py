# ex01.py

def ventall_caracters(c1,c2):
    for c in range(ord(c1),ord(c2)+1):
        yield chr(c)

def szIntrodueixVentall(cInicial,cFinal):
    i = 0
    szR = ""
    for c in ventall_caracters(cInicial,cFinal):
        szR += c
    
    return szR

if __name__ == "__main__":
    print("%s"%szIntrodueixVentall('b','f'))