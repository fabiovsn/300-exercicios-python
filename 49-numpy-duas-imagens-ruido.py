# Elemento de maior valor

import numpy as np

import numpy as np

imagem1 = np.random.randint(low=0,
                            high=256,
                            size=(200, 300, 3),
                            dtype= np.uint8)
imagem2 = np.random.randint(low=0,
                            high=256,
                            size=(200, 300, 3),
                            dtype= np.uint8)

imagem1 = np.expand_dims(imagem1, axis = 0)
imagem2 = np.expand_dims(imagem2, axis = 0)

imagem3 = np.append(imagem1, imagem2, axis = 0)

print(imagem3)
print(imagem3.shape)