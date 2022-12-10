# Nova imagem com cinco primeiras linhas e colunas

import numpy as np

import numpy as np

np.random.seed(42)
array = np.random.randint(low=0,
                      high=2,
                      size=(10, 6))

print(array)
print(f"Números UM encontrados: {np.count_nonzero(array)}")