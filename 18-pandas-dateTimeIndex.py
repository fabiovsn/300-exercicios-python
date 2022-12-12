import pandas as pd
import numpy as np

maio = pd.date_range(start = '2022-05-01',
                     periods = 31)

# Mesmo que pd.date_range(start = '2022-05-01, end = '2022-05-31')

print(maio)