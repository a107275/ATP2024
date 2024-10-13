import random
n = random.randint(0,100)

tentativas = 0
resposta = int(input("Vou pensar num número entre 0 e 100, tenta adivinhar qual é!"))

while resposta != n:

    if resposta > n:
        print("Estou a pensar num número menor. Tenta de novo.")

    elif resposta < n:
        print("Estou a pensar num número maior. Tenta de novo.")

    else:
        print(f"Acertou! Foram necessárias {tentativas} tentativas!")
    tentativas = tentativas + 1