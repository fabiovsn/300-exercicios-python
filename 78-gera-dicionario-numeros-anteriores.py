# Recebe um número e cria dicionário com números anteriores

numero = int(input("Digite um número:\n"))
dicionario = dict()

for i in range(1, numero + 1):
    dicionario[i] = i * i

print(dicionario)