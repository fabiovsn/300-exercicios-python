# Retorno True para cada não numérico

import numpy as np

import numpy as np

A = np.array([0.4, 0.5])
B = np.array([0.39999999, 0.5000001])
C = np.array([0.39, 0.5000001])

if np.allclose(A, B) == True:
    print("Os valores entre A e B são considerados iguais")
if np.allclose(A, C) == True:
    print("Os valores entre A e C são considerados iguais")
if np.allclose(B, C) == True:
    print("Os valores entre B e C são considerados iguais")

print(np.allclose(A, B))
print(np.allclose(A, C))
print(np.allclose(B, C))