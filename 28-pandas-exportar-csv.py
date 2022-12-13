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

dfnumeros[:25].to_csv('data_numeros.csv', sep=',')
dfnumeros2 = pd.read_csv('data_numeros.csv', index_col=0)
print(dfnumeros2)