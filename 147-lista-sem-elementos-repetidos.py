# Gerar nova lista sem elementos repetidos

lista = [
    "a", "a", "a",
    "b", "c", "k",
    "a", 1, 2, 3, 4,
    "j", "l", "m"
]

lista2 = list(set(lista))

print(lista)
print(lista2)