# Interpreta Array

from array import *

lista1 = array("i", [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21])

print(f"Lista1 é composta de {len(lista1)} elementos")

print(f"Lista1 é composta de {lista1.itemsize} bytes")

print(f"Lista1 está alocada na memória no endereço: {lista1.buffer_info()[0]}")