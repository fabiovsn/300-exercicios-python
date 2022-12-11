# Definir casas decimais como 5

import numpy as np

import numpy as np

A = np.array(['1', '2', '3', '4', '5'], dtype=str)

print(np.char.rjust(A, 4, fillchar='0'))