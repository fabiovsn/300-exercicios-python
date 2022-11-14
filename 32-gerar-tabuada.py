# Gerar tabuada

numero = int(input("Digite o número para o qual deseja gerar a tabuada:\n"))

for i in range(0, 11):
    print(f"{numero} X {i} = {numero * i}")
