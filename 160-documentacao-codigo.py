# Documentação de código

def soma(n1, n2):
    """Esta é uma simples função que soma dois números.
    Ao chamar a função, dois números devem ser obrigatoriamente repassados
    para a função, que irá retornar a soma dos números em formato float"""

    return n1 + n2

num1 = float(input("Digite o primeiro número:\n"))
num2 = float(input("Digite o segundo número:\n"))

soma_numeros = soma(num1, num2)

print(f"O resultado da soma entre {num1} e {num2} é: {soma_numeros}")
print(f"Documentação do módulo soma:\n{soma.__doc__}")