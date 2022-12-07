# Elemento de maior valor

import numpy as np

import numpy as np

A = np.array([[4.99, 3.49, 9.99],
              [1.99, 9.99, 14.99],
              [14.99, 2.39, 7.29]])

print(f"Array Original: \n{A}")
print(f"Array Normalizada: \n{np.where(A > 10.0, 10.1, A)}")