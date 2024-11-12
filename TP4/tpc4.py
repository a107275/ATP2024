import random

# função para criar uma lista aleatória
def opcao1():
    num = int(input("Introduza um número para o tamanho da lista:"))
    lista = []
    i = 0
    while i < num:
        x = random.randint(0 , 100)
        lista.append(x)
        i = i + 1
    return lista                      

# função para o utilizador criar uma lista
def opcao2():
    lista = input("Introduza os números da lista (separados por espaços):")     # não colocar int(), manter como string para não dar erro
    return [int(x) for x in lista.split()]                     # vai transformar as strings introduzidas pelo utlizador em inteiros, usando lista.split() para dividi-los através dos espaços

# função para calcular a soma dos elementos a lista
def opcao3(lista):
    soma = 0
    for num in lista:
        soma = soma + num
    return soma

# função para calcular a média dos números da lista
def opcao4(lista):

    if len(lista) > 0:      # primeiro garantir que a lista não está vazia
        soma = opcao3(lista)            # já temos uma função para calcular a soma de todos os números da lista
        return soma / len(lista)        # vai dividir a soma de todos os números pelo tamanho da lista

# função para determinar o maior número da lista
def opcao5(lista):

    if len(lista) > 0:
        maior = lista[0]        # assumir o primeiro índice da lista como o número maior
        for num in lista:       # vai percorrer todos os números da lista, se o número for maior que o "maior" vai substitui-lo
            if num > maior:
                maior = num
        return maior
    
    
# função para determinar o menor número da lista
def opcao6(lista):

    if len(lista) > 0:
        menor = lista[0]        # assumir o primeiro índice da lista como o número menor
        for num in lista:       # vai percorrer todos os números da lista, se o número for menor que o "menor" vai substitui-lo
            if num < menor:
                menor = num
        return menor
    
    else:
        return "A lista está vazia."
    
# função que vai indicar se a lista está por ordem crescente
def opcao7(lista):

    if len(lista) == 1:                 # caso a lista tenha 1 elemento
        return "A lista está ordenada por ordem crescente."
    elif len(lista) == 0:
        return "A lista está vazia, por favor selecione a opção 1 ou 2 para criar uma."
    else:
        for i in range(len(lista) - 1):     # range(stop): vai criar uma sequência de números que começa em 0 e vai até stop - 1; não especificamos o start nem step, então vai assumir o e vai de 1 em 1
                                        # vai até len(lista)-1 porque queremos comparar sempre com o próximo elemento da lista, e a seguir do último não temos com o que comparar
            if lista[i] > lista[i + 1]:
                return "A lista não está ordenada por ordem crescente."
            
        return "A lista está ordenada por ordem crescente."
        
# função que vai indicar se a lista está por ordem decrescente
def opcao8(lista):
    
    if len(lista) == 1:
        return "A lista está ordenada por ordem decrescente."
    elif len(lista) == 0:
        return "A lista está vazia, por favor selecione a opção 1 ou 2 para criar uma."
    else:
        for i in range(len(lista) - 1):
            if lista[i] < lista[i + 1]:
                return "A lista não está ordenada por ordem decrescente."
            
        return "A lista está ordenada por ordem decrescente."

# função que vai procurar um número da lista e diz se o encontra
def opcao9(lista, elem):
    
    for i in range(len(lista)):     # vai percorrer a lista
        if lista[i] == elem:        # se o número for encontrado na lista, vai retornar a sua posição, senão retorna -1
            return i
        else:
            return -1


# função para mostrar o menu
def menu():
    lista = []  # onde se vai armazenar a lista de números

    cond = True
    opcoes = ("1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "0")
    while cond:
        print("1 - Criar lista")
        print("2 - Ler lista")
        print("3 - Soma")
        print("4 - Média")
        print("5 - Número maior")
        print("6 - Número menor")
        print("7 - Está ordenada por ordem crescente?")
        print("8 - Está ordenada por ordem decrescente?")
        print("9 - Procura um elemento")
        print("0 - Sair")

        opcao = input("Introduza o número da opção que pretende escolher:")

        if opcao in opcoes:

            if opcao == "1":      # vai chamar a opção 1 para criar uma lista aleatória
                lista = opcao1()
                print(f"Aqui está a lista: {lista}")

            elif opcao == "2":
                lista = opcao2()  # vai chamar a opção 2 para o utlizador criar uma lista
                print(f"Lista: {lista}")

            elif opcao == "3":
                if len(lista) == 0:
                    print ("A lista está vazia, por favor selecione a opção 1 ou 2 para criar uma.")
                    return menu()
                else:
                    soma = opcao3(lista)  # vai chamar a opção 3 e calcular a soma
                    print(f"A soma de todos os elementos é: {soma}")

            elif opcao == "4":
                if len(lista) == 0:
                    print ("A lista está vazia, por favor selecione a opção 1 ou 2 para criar uma.")
                    return menu()
                else:
                    media = opcao4(lista)  # vai chamar a opção 4 e calcular a média
                    print(f"A média dos elementos é: {media}")

            elif opcao == "5":
                if len(lista) == 0:
                    print ("A lista está vazia, por favor selecione a opção 1 ou 2 para criar uma.")
                    return menu()
                else:
                    maior = opcao5(lista)  # vai chamar a opção 5 e encontrar o maior elemento
                    print(f"O maior elemento é: {maior}")

            elif opcao == "6":
                if len(lista) == 0:
                    print ("A lista está vazia, por favor selecione a opção 1 ou 2 para criar uma.")
                    return menu()
                else:
                    menor = opcao6(lista)  # vai chamar a opção 6 e encontrar o menor elemento
                    print(f"O menor elemento é: {menor}")

            elif opcao == "7":
                if len(lista) == 0:
                    print ("A lista está vazia, por favor selecione a opção 1 ou 2 para criar uma.")
                    return menu()
                else:
                    ordenar = opcao7(lista) # vai chamar a opção 7 e verificar se a lista está ordenada por odem crescente
                    print(ordenar)

            elif opcao == "8":
                if len(lista) == 0:
                    print ("A lista está vazia, por favor selecione a opção 1 ou 2 para criar uma.")
                    return menu()
                else:
                    ordenar = opcao8(lista)  # vai chamar a opção 8 e verificar se a lista está ordenada por odem decrescente
                    print(ordenar)

            elif opcao == "9":        # vai chamar a opcao 9 e procurar o número introduzido na lista
               
                if len(lista) == 0:
                    print ("A lista está vazia, por favor selecione a opção 1 ou 2 para criar uma.")
                    return menu()

                elif len(lista) >= 1:
                    x = input("Introduza o número que quer procurar na lista:")
                    if x != "":         # para garantir que não é vazio
                        elem = int(x)
                        procurar = opcao9(lista, elem)      # procurar vai ser igual a -1 se o número não estiver na litsa, ou igual a "i", a sua posição nela
                        if procurar != -1:
                            print(f"O número {elem} foi encontrado na posição: {procurar}")
                        elif procurar == -1:
                            print("O número não foi encontrado na lista.")
                else:
                    print("Vazio, por favor insira um número!")

           
            elif opcao == "0":
                print(f"Escolheu a opção de sair. A lista final é: {lista}")
                cond = False

        else:
            print("Introduziu uma opção inválida. Por favor, escolha outra opção.")

# vai chamar a função do menu para começar
menu()