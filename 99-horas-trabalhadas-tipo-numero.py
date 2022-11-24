# Gera o valor de salário com base em horas trabalhadas e verifica os tipos numéricos

valor_hora = 29.11
valor_hora_extra = 5

try:
    horas = int(input("Digite o número de horas trabalhadas:\n"))*valor_hora
    adicional = int(input("Digite o número de horas extras:\n"))*valor_hora_extra

    if horas > 40:
        valor_final = horas + adicional
    else:
        valor_final = horas
except:
    print("Digite apenas números...")
    quit()

print(f"Salário base: R$ {horas}")
print(f"Adicional de horas extras: R$ {adicional}")
print(f"Remuneração total: R$ {valor_final}")