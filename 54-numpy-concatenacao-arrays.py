# Nova imagem com cinco primeiras linhas e colunas

import numpy as np

import numpy as np

A = np.array([[3, 4, 5],
              [8, 3, 1]])

B = np.array([[0, 5, 2],
              [4, 2, 1]])

C = np.concatenate((A, B), axis=0)

print(C)