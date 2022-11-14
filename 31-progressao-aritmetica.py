# Progressão Aritmética

termo = int(input("Digite o primeiro termo:\n"))
numero_termos = int(input("Digite o número de termos:\n"))
razao = int(input("Digite a razão:\n"))
pa = termo + ((numero_termos - 1) * razao)

for i in range(termo, pa + 1, razao):
    print(i)