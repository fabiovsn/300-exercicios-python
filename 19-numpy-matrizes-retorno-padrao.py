# Retorno padrão de matrizes

import numpy as np

import numpy as np

A = np.array([[3, 2, 1, 0],
             [6, 2, 1, 6]])

B = np.array([[0, 1, 2, 3, 0],
             [5, 6, 7, 8, 9]])

C = np.array([[True, False, True],
              [True, True, True]])

D = np.array([0.1, 0.4])

for i, j in zip(list("ABCD"), [A, B, C, D]):
    print(f"{i}: {np.all(j, axis=0)}")