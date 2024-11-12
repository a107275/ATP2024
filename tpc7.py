import matplotlib.pyplot as plt


def menu():
    print("-------------------Menu ----------------------")
    print("1- Calcular a média de cada dia")
    print("2- Guardar uma tabela meteorológica num ficheiro de texto")
    print("3- Carregar uma tabela meteorológica de um ficheiro de texto")
    print("4- Calcular a temperatura mínima mais baixa registada na tabela")
    print("5- Calcula a amplitude térmica de cada dia")
    print("6- Calcula o dia em que a precipitaçao foi máxima")
    print("7- Calcula os dias em que a precipitaçao foi maior que o limite p")
    print("8- Calcula o maior número de dias consecutivos em que a precipitaçao esteve abaixo do limite p")
    print("9- Através de uma tabela meteorológica desenha os graficos da Tmín., Tmax., e da pluviosidade.")
    print("0- Sair da aplicaçao.")
    print("------------------------------------------------")


def medias(tabMeteo):
    res = []
    for elem in tabMeteo:                       # elem = elemnto da lista (tabMeteo[])
        media = (elem[1] + elem[2])/2         # elem[1] -T minima; elem[2 - T máxima]
        data = elem[0]
        tuplo = [data, media]
        res.append(tuplo)
    return res


def guardaTabMeteo(t, fnome):
    file = open(fnome, "w")

    for data, min, max, prec in t:
        ano, mes, dia = data
        registo = f"{ano}--{mes}--{dia} | {min} | {max} | {prec}\n"
        file.write(registo)

    file.close()
    return

def carregaTabMeteo(fnome):
    res = []
    file = open(fnome, "r")

    for line in file:
        line = line.strip()

        campos = line.split("|")
        data, min, max, prec = campos       # utilizar unpacking
        ano, mes, dia = data.split("-")     # posso dar unpack logo no split
        tuplo = ((int(ano), int(mes), int(dia)), float(min), float(max), float(prec))
        res.append(tuplo)

    file.close()
    return res

def minMin(tabMeteo):
    minimo = tabMeteo[0][1]
    for data, min, *_ in tabMeteo:
        if min < minimo:
            minimo = min
    return minimo

def amplTerm(tabMeteo):
    res = []
    for elem in tabMeteo:
        amp= (elem[2] - elem[1])
        data = elem[0]
        tuplo = (data, amp)
        res.append(tuplo)
    return res

def maxChuva(tabMeteo):
    data_max = None
    valor_max = 0
    for data, Tmin, Tmax, prec in tabMeteo:
        if prec > valor_max:
            data_max = data
            valor_max = prec
    return(data_max, valor_max)

def diasChuvosos(tabMeteo, p):
    res = []
    for data, min, max, prec in tabMeteo:
        if prec > p:
            tuplo = (data, prec)
            res.append(tuplo)
    return res


def maxPeriodoCalor(tabMeteo, p):
    local_consec = 0            # vai contando os dias consecutivos que a prec é menor que p
    global_consec = 0           # vai guardando o maior número de dias consecutivos consoante a local os conta 
    for data, min, max, prec in tabMeteo:
        if prec < p:
            local_consec = local_consec + 1
        else:
            if local_consec > global_consec:
                global_consec = local_consec
            local_consec = 0

    if local_consec > global_consec:
                global_consec = local_consec

    return global_consec


def grafTabMeteo(t):

    #datas = [f"{data[0]}--{data[1]}--{data[2]}" for data, *_ in t]
    datas = [f"{ano}--{mes}--{dia}" for (ano, mes, dia), *_ in t]
    temps_min = [min for data, min, *_ in t]         # *_ o que não me interessa
    
    temps_max = [max for data, min, max, *_ in t]

    precs = [prec for data, min, max, prec in t]

    plt.plot(datas, temps_min, label = "Temp Mínima", color = "purple", marker = "o")
    plt.plot(datas, temps_max, label = "Temp Máxima", color = "green", marker = "o")
    plt.xlabel("Data")
    plt.ylabel("Temperatura ºC")
    plt.title("Temperatura Mínima")
    plt.legend()
    plt.show()

    plt.bar(datas, precs, color = "orange")
    plt.show()

    plt.bar(datas, precs, label = "Precipitação", color = "c")
    plt.ylabel("Precipitação mm")
    plt.xlabel("Data")
    plt.title("Precipitação")
    plt.legend()
    plt.show()

    return

def main():

    tabMeteo = [((2022,1,20), 2, 16, 0),((2022,1,21), 1, 13, 0.2), ((2022,1,22), 7, 17, 0.01)]
    
    fnome = "meteorologia.txt"
    p = None        

    while True:
        menu()
        opcao = input("Introduza o número da opção que pretende escolher:")

        if opcao == "1":
            res = medias(tabMeteo)
            print(f"Médias de cada dia:{res}")

        elif opcao == "2":
            guardaTabMeteo(tabMeteo, fnome)
            print(f"A tabela foi guardada no ficheiro {fnome}")

        elif opcao == "3":
            tabMeteo = carregaTabMeteo(fnome)
            print(f"Tabela carregada: {tabMeteo}")

        elif opcao == "4":
            res = minMin(tabMeteo)
            print(f"Temperatura mais baixa é {res}")

        elif opcao == "5":
            res = amplTerm(tabMeteo)
            print(f"Amplitude térmica de cada dia: {res}")

        elif opcao == "6":
            res = maxChuva(tabMeteo)
            print(f"O dia com precipitaçao máxima foi: {res}")
        
        elif opcao == "7":
            p = float(input("Introduza um valor para o limite p:"))
            res = diasChuvosos(tabMeteo, p)
            print(f"Os dias com precipitaçao maior que p foram: {res}")
        
        elif opcao == "8":
            p = float(input("Introduza um valor para o limite p:"))
            res = maxPeriodoCalor(tabMeteo, p)
            print(f"O número máximo de dias consecutivos com precipitaçao abaixo de p: {res}")

        elif opcao == "9":
            if tabMeteo:
                grafTabMeteo(tabMeteo)
            else:
                print("Carregue ou insira dados na tabela antes de criar os gráficos.")
        
        elif opcao == "0":
            print("Selecionou sair da aplicação. Até à próxima!")
            return
    
main()