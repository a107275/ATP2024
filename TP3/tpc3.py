import random

# Função que diz como é escolhido o número de fósforos do utlizador:
def num_utilizador(fosforos):        

    jogada = int(input(f"Existem {fosforos} fósforos. Quantos fósforos, entre 1 e 4, quer tirar?"))

    if (jogada >= 1 and jogada <= 4 and jogada <= fosforos):
        return jogada
    
    else:
        print("Número de fósforos inválido. Tenta novamente.")
        return num_utilizador(fosforos)

# Função que diz como é escolhido o número de fósforos do computador (caso jogue em primeiro ou não):
def num_computador(fosforos, primeiro = False):          

    if fosforos == 1:
          jogada = 1
    
    elif primeiro:          # Tentar deixar multiplos de 5
        jogada = (fosforos - 1) % 5

        if jogada < 1 or jogada > 4:        # Para garantir que a jogada é válida, se não der múltiplos de 5, faz uma jogada aleatória
            if fosforos < 4:
                    jogada = random.randint(1, fosforos)     # Se fosforos < 4
            else:
                    jogada = random.randint(1, 4)            # Se fosforos >= 4

    else:       # Quando o computador vai jogar em segundo, tenta garantir deixar um múltiplo de 5 
          jogada = (fosforos - 1) % 5

          if jogada == 0:       # Se não der para ser múltiplo de 5, tenta tirar o mínimo
                jogada = 1
    
    print(f"O computador tirou {jogada} fósforos.")
    return jogada

# Função que diz como vai funcionar o jogo no modo 1 (o utlizador tira primeiro):
def utilizador(fosforos):
    while fosforos > 0:

        # Turno do jogador  
        jogada_u = num_utilizador(fosforos)     
        fosforos = fosforos - jogada_u

        if fosforos == 0:
            print("Tiraste o último fósforo! Perdeste.")
            return

        # Turno do computador
        jogada_c = num_computador(fosforos, primeiro = False)
        fosforos = fosforos - jogada_c

        if fosforos == 0:
            print("O computador tirou o último fósforo! Ganhaste!")
            return

# Função que diz como vai funcionar o jogo no modo 2 (o computador tira primeiro):
def computador(fosforos):
    while fosforos > 0:
                                                
        # Turno do computador
        jogada_c = num_computador(fosforos, primeiro = True)
        fosforos = fosforos - jogada_c

        if fosforos == 0:
            print("O computador tirou o último fósforo! Ganhaste!")
            return

        # Turno do jogador
        jogada_u = num_utilizador(fosforos)
        fosforos = fosforos - jogada_u

        if fosforos == 0:
            print("Tiraste o último fósforo! Perdeste.")
            return

# Função do menu do jogo:
def menu():
    fosforos = 21
    print("Bem-vindo ao jogo dos 21 fósforos!")
    modo_do_jogo = int(input("Escolha o modo de jogo: 1- O utilizador começa; 2- O computador começa:"))

    if modo_do_jogo == 1:       # O utilizador começa
        utilizador(fosforos)
    elif modo_do_jogo == 2:     # O computador começa
        computador(fosforos)
    else:
        print("Modo inválido. Escolha entre 1 e 2.")
        menu()  # «Se a escolha for inválida vai chamar o menu outra vez

# Chamar o menu para o jogo começar
menu()