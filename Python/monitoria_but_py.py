#Código
numParticipantes = int(input("Número de participantes do bolão: ")
numJogos = int(input("Número de jogos: "))
participantes = []
resultadosCorretos = [1, 0, 3, 4, 1, 2, 3, 6]


for i in range(0, numParticipantes):
    nomeParticipante = input("Nome do participante")
    participantes += nomeParticipante
    resultsProv = []
    print("Agora, para os chutes do participante")
    for i in range(0, numJogos):
        gol = int(input("Gols Time 1: "))
        resultsProv += gol
        gol = int(input("Gols Time 2: "))
        resultsProv += gol


#Velho (Revisar e adaptar)
resultados = [1, 0, 3, 4, 1, 0, 1, 1, 1, 0]
participantes = []
bolao = []
pontos_final = []
total = 0
players_am = int(input("Quantidade jogadores: "))
reps = 0
iterations = 0
rept = 0
while reps < players_am:
    participantes.append(str(input("Nome: ")))

    while len(pontos_final) < players_am:
        while len(bolao) != len(resultados):
            bolao.append(int(input("Gols Mandante:\n")))
            bolao.append(int(input("Gols Visitante:\n")))

        while iterations < len(resultados):
            if bolao[iterations] == resultados[iterations] and bolao[iterations+1] == resultados[iterations+1]:
                total+=5
                iterations+=2
            elif bolao[iterations] == bolao[iterations+1] and resultados[iterations] == resultados[iterations+1] and bolao[iterations] != resultados[iterations]:
                total+=2
                iterations+=2
            elif (bolao[iterations] > bolao[iterations+1] and resultados[iterations] > resultados[iterations+1]) or (bolao[iterations] < bolao[iterations+1] and resultados[iterations] < resultados[iterations+1]):
                total+=3
                iterations+=2
            else:
                iterations+=2
            pontos_final.append(total)
            print(pontos_final)
    while rept < len(pontos_final):
        if pontos_final[rept] > pontos_final[rept+1]:
            vencedor = pontos_final[rept]
            rept+=1
        else:
            vencedor = pontos_final[rept+1]
            rept+=1
    reps+=1
    bolao = []

print(f"O vencedor foi: {participantes.index(ind)} com {vencedor} pontos")
