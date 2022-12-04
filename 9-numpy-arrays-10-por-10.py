# Array 10 x 10

import numpy as np

array = np.full(shape=(10, 10),
                fill_value=128,
                dtype=float)

print(array)
print(type(array[0, 0]))