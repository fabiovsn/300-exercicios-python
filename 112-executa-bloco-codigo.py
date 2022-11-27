# Executa bloco de código

codigo = ""

num = int(input("Digite um número:\n"))

def eleva_ao_quadrado(num):
    return num**2

print(f"{num} elevado ao quadrado é: {eleva_ao_quadrado(num)}")

exec(codigo)