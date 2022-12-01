# Calcula quantidade de números em texto

import re

texto = "Python 3.9"

numeros = re.findall(pattern=r'\d', string=texto)

print(f"Foram encontrados {len(numeros)} números no texto '{texto}'")
print(f"Os números são {numeros[0]} e {numeros[1]}, respectivamente")