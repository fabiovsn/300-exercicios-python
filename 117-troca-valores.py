# Troca posições de primeiro e último elemento da lista

lista1=[11, 22, 33, 44, 55, 66, 77, "x"]

print(f"Lista original: {lista1}")

temp = lista1[0]
lista1[0] = lista1[-1]
lista1[-1] = temp

print(f"Lista final: {lista1}")