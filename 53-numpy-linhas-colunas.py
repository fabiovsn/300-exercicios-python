# Nova imagem com cinco primeiras linhas e colunas

import numpy as np

import numpy as np

imagem1 = np.random.randint(low=0,
                           high=256,
                           size=(10, 10, 3),
                           dtype=np.uint8)

imagem2 = imagem1[:5, :5, :]

print(imagem2)