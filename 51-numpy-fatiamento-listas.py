# Fatiamento de listas

import numpy as np

import numpy as np

array = np.arange(4, dtype='int').reshape(-1, 2)
print(array)

array = array[::-1, ::-1]
print(array)