'''
#include <stdio.h>

void vMenu(){
    printf("1) Hola\n");
    printf("2) Adeu\n");
    printf("3) Surt\n");
}

int nQuinaOpcio(){
    int n;

    printf("\n\nEscolliu una opcio: ");
    scanf("%d", &n);

    return n;
}

void vPensa(int nO){
    switch(nO){
        case 1: printf("Hola\n");
                break;
        case 2: printf("Adeu\n");
                break;
        case 3: printf("Surto\n");
                break;
        default: printf("Manca de comprensió lectora?\n");
    }
}
'''

def vMenu():
    print("1) Hola")
    print("2) Adeu")
    print("3) Surt")

def nQuinaOpcio():
    n = int(input("Escolliu una opcio: "))
    return n

def vPensa(nO):
    if nO == 1:
        print("Hola")
    elif nO == 2:
        print("Adeu")
    elif nO == 3:   
        print("Surto")
        print("Manca de comprensió lectora?")

