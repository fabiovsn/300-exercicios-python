import pandas as pd
import numpy as np

num = pd.Series(data = np.arange(0, 20, 2),
                index = np.arange(0, 10),
                dtype = 'float')

print(num)