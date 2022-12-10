# Definir casas decimais como 5

import numpy as np

import numpy as np

np.random.seed(42)
array = np.array([["ID", "preco"],
                  ["001", 14.99],
                  ["002", 4.99],
                  ["003", 7.99],
                  ["004", 2.49],
                  ["005", 1.49]])

np.random.shuffle(array[1:])
print(array)