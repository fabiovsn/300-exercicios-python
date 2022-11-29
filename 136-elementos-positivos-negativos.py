# Organizar números positivos e negativos

lista1 = [-1, 6, -9, -8, 4, 0, -3, 2, 7, 1, 8, -2]

print(f"Lista original: {lista1}")

lista2 = [x for x in lista1 if x < 0] + [x for x in lista1 if x >= 0]
lista3 = [x for x in lista1 if x < 0]
lista4 = [x for x in lista1 if x >= 0]

print(f"Lista rearranjada: {lista2}")
print(f"Elementos negativos: {lista3}")
print(f"Elementos positivos: {lista4}")