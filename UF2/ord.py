def incrementaUnNum(txt):
    retorn=""
    for c in txt:
        if c >= '0' and c <='8':
            retorn += chr(ord(c)+1)
        elif c == '9':
            retorn += '0'
        else:
            retorn += c
    return retorn

text = input("Escriu un text: ")
print(incrementaUnNum(text))
