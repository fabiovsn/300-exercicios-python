# Array 5 x 5

import numpy as np

import numpy as np

A = np.arange(20, 45).reshape(5, 5)
np.save("array.npy", A)

B = np.load("array.npy")
print(B)