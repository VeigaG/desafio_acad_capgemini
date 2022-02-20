'''Débora se inscreveu em uma rede social para se manter em contato com seus amigos.
A página de cadastro exigia o preenchimento dos campos de nome e senha, porém a senha precisa ser forte.
O site considera uma senha forte quando ela satisfaz os seguintes critérios:
Possui no mínimo 6 caracteres.
Contém no mínimo 1 digito.
Contém no mínimo 1 letra em minúsculo.
Contém no mínimo 1 letra em maiúsculo.
Contém no mínimo 1 caractere especial. Os caracteres especiais são: !@#$%^&*()-+
Débora digitou uma string aleatória no campo de senha, porém ela não tem certeza se é uma senha forte.
Para ajudar Débora, construa um algoritmo que informe qual é o número mínimo de caracteres que devem ser adicionados para uma string qualquer ser considerada segura.'''



def d_senha():
    global senha
    senha = input('\nDigite sua senha: ')
     
def cont_caracter():
    global falta
    list(senha)
    cont = 0
    min = 6
    for i in range(0, len(senha)):
        if senha[i]== " ":#verifica espaços em branco
            print('Espaços em branco não são aceitos.\nTente novamente!\n')
            d_senha()
        else:
            cont+= 1 #conta quantos caracteres foram digitados
    if cont < min:
        falta = min - cont #calcula quantos caracteres falta para a qnt minima de itens
        return True
    else:
        return False
   
def digito():
    if not any(i.isdigit() for i in senha):#verifica se existe ao menos 1 numero. any()verifica se ao menos 1 dos elementos é verdadeiro
        return True
    else:
        return False
   
def minusc():
    if not any(i.islower() for i in senha):#verifica se existe ao menos 1 letra minuscula
        return True
    else:
        return False

def maiusc():
    if not any(i.isupper() for i in senha):#verifica se existe ao menos 1 letra maiuscula
        return True
    else:
        return False

def caracter():    
    simbol = ['!','@','#','$','%','^','&','*','(',')','-','+']
    if not set(simbol) & set(senha):#compara as listas e verifica se existe ao menos 1 dos caracteres da lista caracter na senha informada
        return True
    else:
        return False

def teste():
    while (cont_caracter() or digito() or minusc() or maiusc() or caracter()) == True:

        print("\nA senha deve conter no mínimo:")
             
        if cont_caracter() == True:
            print("6 caracteres. Insira mais %d caracter(es)." %falta)
        if digito() == True:
            print('1 número.')
        if minusc() == True:
            print('1 letra minúscula.')
        if maiusc() == True:
            print('1 letra maiúscula.')
        if caracter() == True:
            print('1 dos caracteres [!@#$%^&*()-+].')

        d_senha()
   
    print('\nDados Salvos com sucesso!')


d_senha()
teste()