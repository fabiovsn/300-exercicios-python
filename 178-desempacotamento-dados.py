# Desempacotamento de dados

from pydash import py_

lista1 = [[1, 2, [3, 4, 5, 6, 7, 8]], [9, 10, 11, 12]]
lista2 = py_.flatten_deep(lista1)

print(lista1)