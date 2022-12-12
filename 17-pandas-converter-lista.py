import pandas as pd
import numpy as np

data = ['01', '02', '03', '04', '05']

pddata = pd.Series(data = data)
print(type(pddata[0]))

pddata = pd.to_numeric(pddata)
# Mesmo que: pddata = pddata.astype(int)

print(type(pddata[0]))

print(pddata)