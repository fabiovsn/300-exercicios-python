# Recebe um nome e duas notas e salva em lista

from operator import itemgetter

nomes=[]

while True:
    dados = input("Digite seu nome seguido de duas notas de 0 a 10.\n")
    if not dados:
        break
    nomes.append(tuple(dados.split(",")))

print(sorted(nomes, key = itemgetter(0, 1, 2)))