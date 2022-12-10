# Nova imagem com cinco primeiras linhas e colunas

import numpy as np

import numpy as np

A = np.random.randint(low=0,
                      high=10,
                      size=(5, 8))

print(A)

A1, A2, A3 = np.split(A, [2, 6], axis=1)

print(A1)
print(A2)
print(A3)