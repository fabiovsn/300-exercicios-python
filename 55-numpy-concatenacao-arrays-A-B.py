# Nova imagem com cinco primeiras linhas e colunas

import numpy as np

import numpy as np

A = np.array([[4.3, 4.2],
              [3.1, 3.6]])

B = np.array([[0], [1]])

C = np.concatenate((A, B), axis=1)

print(C)