import pandas as pd
import numpy as np

maio = pd.date_range(start='2022-05-01',
                     periods=31)

hmaio = pd.DataFrame(data = maio,
                     columns=['Data'])

hmaio['Dia do ano'] = hmaio['Data'].dt.dayofyear

print(hmaio)