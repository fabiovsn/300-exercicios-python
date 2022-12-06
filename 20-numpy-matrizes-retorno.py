# Retorno padrão de matrizes

import numpy as np

import numpy as np

A = np.array([[0, 0, 0],
             [0, 0, 0]])

B = np.array([[0, 0, 0],
             [0, 1, 0]])

C = np.array([[False, False, False],
              [True, False, False]])

D = np.array([[0.1, 0.0],
              [0.0, 0.2]])

for i, j in zip(list("ABCD"), [A, B, C, D]):
    print(f"{i}: {np.any(j)}")
    print(f"{i}: {np.any(j, axis=0)}")