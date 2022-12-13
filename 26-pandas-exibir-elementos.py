import pandas as pd
import numpy as np

numeros = {'normal': np.random.normal(loc = 0,
                                      scale = 1,
                                      size = 50),
           'uniforme': np.random.uniform(low = 0,
                                          high = 1,
                                          size = 50),
           'binomial': np.random.binomial(n=1,
                                          p=0.2,
                                          size=50)}

dfnumeros = pd.DataFrame(data = numeros).reset_index()
dfnumeros.columns = ['indice', 'normal', 'uniforme', 'binomial']
dfnumeros = dfnumeros.set_index('indice')

#print(dfnumeros)
print(dfnumeros.head(5))
print()
print(dfnumeros.tail())