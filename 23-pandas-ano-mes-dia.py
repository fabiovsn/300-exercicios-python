import pandas as pd
import numpy as np

maio = pd.date_range(start='2022-05-01',
                     periods=31)

hmaio = pd.DataFrame(data = maio,
                     columns=['Data'])

hmaio['Ano'] = hmaio['Data'].dt.year
hmaio['Mes'] = hmaio['Data'].dt.month
hmaio['Dia'] = hmaio['Data'].dt.day

hmaio = hmaio.drop(columns=['Data'])

print(hmaio)