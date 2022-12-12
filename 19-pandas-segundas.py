import pandas as pd
import numpy as np

segundas = pd.date_range(start = '2020-01-01', end = '2022-06-01', freq= 'W-MON')

print(segundas)
print(f'Entre 01/2020 e 06/2020 existem {len(segundas)} segundas-feiras')