# Exibir mensagem de acordo com validação

num1 = int(input("Digite o primeiro número:\n"))
num2 = int(input("Digite o segundo número:\n"))

if num1 > num2:
    print("O primeiro número é maior que o segundo.")
elif num2 > num1:
    print("O segundo número é maior que o primeiro")
else:
    print("Números iguais")