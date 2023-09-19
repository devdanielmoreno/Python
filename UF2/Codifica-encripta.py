#codifica00.py 
def szIncrementaCaracterDeCadena(text):
    codif = ""
    for c in text:
        if c != ' ':
            if c == 'Z':
                codif += 'A'
            elif c == 'z':
                codif += 'a' 
            else:
                codif += chr(ord(c)+1)
        else:
            codif += ' '
    return codif
                

szText = input("Escriviu un text per a codificar: ")
print("Heu escrit: \"%s\""%szText)
print('Heu escrit: "%s"'%szText) 
szCodificat = szIncrementaCaracterDeCadena(szText)
print('Codificat: "%s"'%szCodificat) 
