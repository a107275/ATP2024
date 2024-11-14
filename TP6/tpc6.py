def menu():
    print("---------------MENU---------------\n Opção 1 - Criar turma\n Opção 2 - Inserir aluno na turma\n Opção 3 - Listar a turma\n Opção 4 - Identificar um aluno pelo id\n Opção 5 - Guardar a turma em ficheiro\n Opção 6 - Carregar uma turma dum ficheiro\n Opção 0 - Sair")


# 1- Função para criar uma turma
def criarTurma():   # a turma vai ser uma lista de alunos
    turma = []
    return turma

# 2- Função para inserir um aluno na turma
def insereAluno(turma):
    
    nome = input("Introduza o nome do aluno:")
    id_aluno = input("Introduza o id do aluno:")
    for aluno in turma:
        if aluno[1] == id_aluno:
            print(f"O aluno com o ID {id_aluno} já está na turma.")
            return turma
        
    notas = []
    for elem in ("notaTPC" , "notaProj" , "notaTeste"):
            nota = float(input(f"Introduza a {elem}:"))
            notas.append(nota)

    aluno = (nome, id_aluno, notas)    # cada aluno é representado por um tuplo
    turma.append(aluno)
    print(f"O/A aluno/a {nome} foi inserido/a com sucesso na turma!")
    return turma

# 3- Função para listar uma turma
def listarTurma(turma):
    if not turma:
        print("A turma está vazia")
    else:
        for aluno in turma:
            nome, id_aluno, notas = aluno       # unpacking do tuplo
            print(f"Nome: {nome}    | ID: {id_aluno} | Notas: {notas}")

# 4- Função para consultar aluno por id
def consultarAluno (turma, id_aluno):
    encontrado = False
    for aluno in turma:
        if aluno[1] == id_aluno:     #indice 1 correpsonde ao id
            nome, _, notas = aluno

            print(f"Nome: {nome}    | ID: {id_aluno} | Notas: {notas}")
            encontrado = True
    if not encontrado:
        print(f"O aluno com ID {id_aluno} não foi encontrado.")

    return encontrado

# 5-Função para guardar a turma num ficheiro
def turmaFicheiro(turma, nomeFicheiro):
    f = open(nomeFicheiro, 'w', encoding = 'utf-8')  
    # Open para abriri o ficheiro   
    # write, Abre o ficheiro para escrita se o ficheiro já existir, ele será sobrescrito (o conteúdo anterior será apagado)./ Se o ficheiro não existir, ele será criado
    
    # Para percorrer a lista dos alunos e depois escrever no ficheiro
    for aluno in turma:
        nome, id_aluno, notas = aluno
        f.write(f"{nome}, {id_aluno},{notas[0]}, {notas[1]}, {notas[2]}\n")

    f.close()   # Fechar o ficheiro
    print(f"A turma foi guardada no ficheiro {nomeFicheiro}.")
    

# 6- Função para carregar uma turma de um ficheiro
def carregarTurma(nomeFicheiro):
    turma = []  # lista vazia para armazenar
    f = open(nomeFicheiro, 'r') # abriri o ficheiro para ler

    if f:
        for linha in f:
            parametro = linha.strip().split(',') # para tirar os espaços em branco e dividir as linhas em parametros usando virgulas

            if len(parametro) == 5: 
                nome = parametro[0]
                id_aluno = parametro[1]
    
    # para tranformar as notas de texto (string) em inteiros (int) e guardar numa lista
                notas =  [float(parametro[2]) , float(parametro[3]) , float(parametro[4])]
           
                turma.append((nome, id_aluno, notas)) # adicionar como tuplo à lista
    
        f.close() # Fechar o ficheiro
        print(turma)
        return turma # Retorna a lista

def main():
    turma = []
    cond = True
    opcoes = ("1", "2", "3", "4", "5", "6", "0")
    while cond:
        menu()
        opcao = input("Introduza o número da opção que deseja:")
        if opcao in opcoes:
            if opcao == "1":
                turma = criarTurma()
                print("A turma foi criada com sucesso.")

            if opcao == "2":
                turma = insereAluno(turma)

            if opcao == "3":
                listarTurma(turma)

            if opcao == "4":
                id_aluno = input("Introduza o ID do aluno:")
                res = consultarAluno(turma, id_aluno)
                print(res)
            

            if opcao == "5":
                nomeFicheiro = input("Introduza o nome do ficheiro para guardar a turma:")
                turmaFicheiro(turma, nomeFicheiro)
            
            if opcao == "6":
                nomeFicheiro = input("Introduza o nome do ficheiro para carregar a turma:")
                turma = carregarTurma(nomeFicheiro)
                print (f"A tua turma foi carregada do ficheiro {nomeFicheiro} com sucesso!")
            
            if opcao == "0":
                cond = False
                print("Escolheu a opção de sair. Até à próxima!")
main()
