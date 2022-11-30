# Gerar dicionário com valor padrão

n = int(input("Digite um número:\n"))

d = dict()

for i in range(1, n + 1):
    d[i] = i * i

print(d)