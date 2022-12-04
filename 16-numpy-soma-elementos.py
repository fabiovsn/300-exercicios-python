# Soma elementos array

import numpy as np

arr = np.arange(20, 45).reshape(5, 5)
soma_linhas = arr.sum(axis = 1)
soma_colunas = arr.sum(axis = 0)

print(arr)
print(f"Soma dos elementos da primeira linha: {soma_linhas[0]}")
print(f"Soma dos elementos da primeira coluna: {soma_colunas[0]}")
print(f"Soma dos elementos da quarta linha: {soma_linhas[3]}")
print(f"Soma dos elementos da quarta coluna: {soma_colunas[3]}")