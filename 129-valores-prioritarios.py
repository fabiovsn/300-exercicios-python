# Extrair valores prioritários

import heapq as hq

fila_original = [23, 45, 60, 19, 23, 50, 18, 82, 46, 77]
fila_normal = hq.nsmallest(7, fila_original)

fila_prioritaria = list(set(fila_original)-set(fila_normal))
fila_prioritaria2 = hq.nlargest(3, fila_original)


print(f"Fila Normal: {fila_normal}")

print(f"Fila Prioritária: {fila_prioritaria}")

print(f"Fila Prioritária 2: {fila_prioritaria2}")