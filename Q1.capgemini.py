'''Escreva um algoritmo que mostre na tela uma escada de tamanho n utilizando o caractere * e espaços.
A base e altura da escada devem ser iguais ao valor de n. A última linha não deve conter nenhum espaço.'''

def escada(numero):
    x = numero - 1    
    for i in range(1, numero+1):
        linha = (x * " " + i * "*")
        print(linha)
        x = x-1

def inicio():
    numero = int(input("\nInforme o tamanho da escada: "))
    escada(numero)
    replay = str(input("\nInformar outro tamanho? [s/n] ").lower())
    if replay == "s":
        inicio()
    elif replay == "n":
        print("\nObrigada pela contribuição!")
    else:
        print("\nComando inválido! Até mais!")

inicio()
