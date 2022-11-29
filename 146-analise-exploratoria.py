# Ferramenta simples de análise exploratória

from statistics import median, variance, stdev

lista=[
    -1505, 2518, 2333, 4682, -1740, 1067, 995, 22, 2,
    -1153, -4098, 4560, 2958, 3640, -4154, 2345, 4,
    -1601, 158, -4044, -98, 707, 359, -3088, 527,
    -3004, -4045, 563, -4137, 4598, -3862, 488, -1
]

print(f"O maior número é: {max(lista)}")
print(f"O menor número é: {min(lista)}")
print(f"A soma de todos os números é: {sum(lista)}")
print(f"A quantidade de elementos da lista é: {len(lista)}")
print(f"A média aritmética é: {sum(lista)/len(lista):.2f}")
print(f"Mediana: {median(lista):.2f}")
print(f"Variância: {variance(lista):.2f}")
print(f"Desvio padrão: {stdev(lista):.2f}")