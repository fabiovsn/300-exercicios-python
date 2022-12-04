# Soma elementos array

import numpy as np

A = np.array([[3, 2, 1, 4],
             [5, 2, 1, 6]])

B = np.array([[0, 1, 2, 3, 4],
             [5, 6, 7, 8, 9]])

C = np.array([[True, False, False],
              [True, True, True]])

D = np.array([0.1, 0.3])

for i, j in zip(list("ABCD"), [A, B, C, D]):
    print(f"Array {i}: {np.all(j)}")