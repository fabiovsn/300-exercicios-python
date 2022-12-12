import pandas as pd
import numpy as np

n_horas_maio = pd.date_range(start='2022-05-01',
                             end='2022-06-01',
                             freq='H')

print(n_horas_maio)
print(f'Maio de 2022 possui um total de {len(n_horas_maio) - 1} horas')