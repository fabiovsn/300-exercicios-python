# Soma arrays

import numpy as np

arr = np.arange(20, 45).reshape(5, 5)
array10_soma = arr.sum()
array10_desvio = arr.std()

print(arr)
print(f"A soma de todos os elementos é: {array10_soma}")
print(f"O valor do desvio padrão é: {array10_desvio}")