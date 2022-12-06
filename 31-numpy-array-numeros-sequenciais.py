# Array de números sequenciais

import numpy as np

import numpy as np

A = np.arange(12, dtype = "int").reshape(-1 , 4)
np.savetxt(fname="array.txt",
           X = A,
           fmt = "%0.2f")

B = np.loadtxt("array.txt")
print(B)