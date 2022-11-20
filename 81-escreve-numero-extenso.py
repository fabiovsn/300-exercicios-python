# Escreve número por extenso

def num_p_texto(n):
    if n == 0:
        return "zero"

    unidade = ("", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove")

    dezena = (",", "vinte e ", "trinta e ", "quarenta e ", "cinquenta e ", "sessenta e ", "setenta e ", "oitenta e ", "noventa e ")

    dez_x = ("dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove")

    h, t, u = "", "", ""

    if n == 100:
        h = unidade[0] + "cem"
        n = n % 100
    elif n >= 20:
        t = dezena[(n//10 - 1)]
        n = n % 10
    elif n > 10:
        t = dez_x[n - 10]
        n = 0

    u = unidade[n]
    return "".join(filter(None, [h, t, u]))

num = int(input("Digite o número menor que cem a ser convertido:\n"))
if num <= 100:
    print(f"{num} por extenso é: {num_p_texto(num)}")
else:
    print("Número inválido")