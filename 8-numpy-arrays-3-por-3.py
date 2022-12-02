# Array 3 x 3

import numpy as np

array = np.arange(9)
array = array.reshape(3, 3)

# Mesmo que:
# array = np.arange(9).reshape(3)

print(array)