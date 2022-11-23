# Retorna se número digitado é perfeito

x = int(input("Digite um número:\n"))

def num_perfeito(x):
    soma = 0
    for i in range(1, x):
        if x % i == 0:
            soma += i

    return soma == x

if num_perfeito(x):
    print(f"{x} é um número perfeito!!")
else:
    print(f"{x} não é um número perfeito!!")