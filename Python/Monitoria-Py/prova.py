def inputJogos(times, linhaIns):
    print("Para inserir os resultados, siga a regra:")
    print("GolsTime1 x GolsTime2 \n")

    listaPot = []  # lista de potências já usadas (evitar repetição de jogos)
    n = 1  # índice do jogo

    for i in range(len(times)):
        for j in range(i + 1, len(times)):  # Garantir que o confronto não seja repetido
            print(f"Jogo {n}: {times[i]} x {times[j]}")
            n += 1
            tempRes = input(f"{times[i]} x {times[j]}: ").lower().split(" x ")
            linhaIns.append((int(tempRes[0]), int(tempRes[1])))  # Adiciona o placar dos jogos por tuplas numa linha da matriz

def calcPont(previsao, resultados):
    pontos = 0
    for i in range(len(resultados)):
        resultado_jogo = resultados[i]
        previsao_jogo = previsao[i]

        if previsao_jogo[0] == resultado_jogo[0] and previsao_jogo[1] == resultado_jogo[1]:
            pontos += 5  # Placar exato
        elif (previsao_jogo[0] > previsao_jogo[1] and resultado_jogo[0] > resultado_jogo[1]) or (previsao_jogo[0] < previsao_jogo[1] and resultado_jogo[0] < resultado_jogo[1]):
            pontos += 3  # Acertar vencedor
        elif previsao_jogo[0] == previsao_jogo[1] and resultado_jogo[0] == resultado_jogo[1]:
            pontos += 2  # Empate, mas placar errado
    return pontos

# Lista de times
times = ["Vasco", "Bangu", "Flamengo"]

qtdJog = int(input("Quantidade de jogadores: "))
prevBol = []

matrPrin = [[], [], []]
# matrPrin
# |[nomes participantes ]|
# |[matrPrin jogos      ]|
# |[pontos participantes]|

# Registrando nome dos participantes
for i in range(qtdJog):
    participante = input(f"Nome participante {i+1}: ")
    matrPrin[0].append(participante)

# Guardando resultados corretos
print("\nResultados corretos dos jogos\n")
inputJogos(times, matrPrin[1])
print()

# previsões dos participantes
for i in range(qtdJog):
    print(f"Bolão do {matrPrin[0][i]}: ")
    previsoes = []
    inputJogos(times, previsoes)
    prevBol.append(previsoes)

# calculando pontos de cada participante
for i in range(qtdJog):
    pontos = calcPont(prevBol[i], matrPrin[1])
    matrPrin[2].append(pontos)

# exibindo resultados finais
for i in range(qtdJog):
    print(f"\n{matrPrin[0][i]} - Pontos: {matrPrin[2][i]}")

print("\nMatriz final:")
print(matrPrin)
