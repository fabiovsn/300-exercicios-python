def soma(*args):
    soma = 0
    for item in args:
        soma += item

    print(f"O resultado da soma é: {soma}")

soma = soma(2, 2, 10)

