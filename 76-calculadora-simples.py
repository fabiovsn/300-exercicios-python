# Calculadora simples

print("Calculadora de 4 operações")

print("+ -> Soma")
print("- -> Subtração")
print("* -> Multiplicação")
print("/ -> Divisão")

a = float(input("Digite o primeiro número:\n"))
b = float(input("Digite o segundo número:\n"))

operacao = input("Digite a operação a realizar( + , - , * ou / ):")

if operacao == "+":
    soma = a + b
    print(f"O resultado da soma é: {soma}")
elif operacao == "-":
    subtracao = a - b
    print(f"O resultado da subtração é: {subtracao}")
elif operacao == "*":
    multiplicacao = a * b
    print(f"O resultado da multiplicação é: {multiplicacao}")
elif operacao == "/":
    divisao = a / b
    print(f"O resultado da divisão é: {divisao}")
else:
    print("Operação inválida!")






