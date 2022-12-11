# Definir casas decimais como 5

import numpy as np

import numpy as np

A = np.array(['001', '002', '003'], dtype=str)
B = np.array(['XC', 'YC', 'ZC'], dtype=str)
C = np.char.add(A, B)

print(C)