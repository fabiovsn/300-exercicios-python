# Array de loteria

import numpy as np

import numpy as np

np.random.seed(2042)
array = np.random.choice(range(1, 50),
                         size = 6,
                         replace = False)

print(array)