# Médias estatísticas

import statistics
import numpy as np

data = [59.19, 72.05, 66.82, 81.15, 66.33, 94.87, 99.65, 70.13, 55.75]

print(f"Média simples: {round(statistics.mean(data),5)}")
print(f"Média harmônica: {round(statistics.harmonic_mean(data),5)}")

data = np.array(data)
media_geom = round(data.prod()**(1.0/len(data)), 5)

print(f"Média geométrica: {media_geom}")