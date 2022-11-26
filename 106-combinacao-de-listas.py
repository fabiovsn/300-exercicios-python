# Combinação de duas listas

lista1 = []

for x in [1, 2, 3]:
    for y in [4, 5, 6]:
        if x != y:
            lista1.append((x, y))

print(lista1)

# alternativa

lista2 = [(x, y) for x in [1, 2, 3] for y in [4, 5, 6] if x != y]

print(lista2)