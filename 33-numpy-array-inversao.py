# Array de números sequenciais

import numpy as np

import numpy as np

A = np.arange(12, dtype="int").reshape(-1, 4)
A_inv = A[::-1]

print(A_inv)