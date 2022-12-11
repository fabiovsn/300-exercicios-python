import pandas as pd

nomes = ['Anna', 'Fernando', 'Maria', 'Paulo', 'Tânia']

pdnomes = pd.Series(data = nomes)

print(pdnomes)
print(type(pdnomes))