# Números divisíveis por 7 e múltiplos de 5

numeros = []

for numero in range(0, 501):
    if(numero % 7 == 0) and (numero % 5 == 0):
        numeros.append(str(numero))

print(",".join(numeros))