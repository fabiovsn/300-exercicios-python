# Contagem números ímpares

contador = 0
soma = 0

for i in range(1, 101):
    if i % 2 != 0:
        print(i)
        soma += i
        contador += 1

print(f"Foram encontrados {contador} números ímpares")
print(f"A soma desses números é {soma}")
