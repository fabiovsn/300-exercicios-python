import pandas as pd

estoque = {'Cel Xiaomi Redmi Note 11': 1699,
           'Cel Samsung Galaxy s22': 3999,
           'Cel Motorola Moto G200': 2999,
           'Cel LG V60 ThinQ': 1999}

pdestoque = pd.Series(data = estoque)
pdestoque = pd.DataFrame(pdestoque, columns= ['Preço'])

print(pdestoque)
print(type(pdestoque))