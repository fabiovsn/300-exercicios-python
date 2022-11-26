# Controlador de direção

import math

posicao = [0, 0]

while True:
    coordenada = input("Digite a coordenada, seguido do número de passos\n")

    if not coordenada:
        break

    movimento = coordenada.split(" ")
    direcao = movimento[0]
    passos = int(movimento[1])

    if direcao == "CIMA":
        posicao[0] += passos
    elif direcao == "BAIXO":
        posicao[0] -= passos
    elif direcao == "ESQUERDA":
        posicao[1] -= passos
    elif direcao == "DIREITA":
        posicao[1] += passos
    else:
        pass

print(int(round(math.sqrt(posicao[1]**2 + posicao[0]**2))))
print(posicao)
