# Verifica conteúdo e identificador na memória

import collections

c1 = (2, 4, 6, 8, 10)

dq1 = collections.deque(c1)

c2 = (2, 4, 6, 8, 10)
dq2 = collections.deque(c2)

c3 = dq2

print(f"Conjunto 1: {dq1}")
print(f"Endereço do Conjunto 1: {id(dq1)}")

print(f"Conjunto 1: {dq2}")
print(f"Endereço do Conjunto 1: {id(dq2)}")

print(f"Conjunto 1: {c3}")
print(f"Endereço do Conjunto 1: {id(c3)}")

if (dq1 == dq2) and (id(dq1) == id(dq2)):
    print("Conjunto 1 e Conjunto 2 possuem os mesmos elementos e são o mesmo objeto alocado em memória")

if (dq1 == c3) and (id(dq1) == id(c3)):
    print("Conjunto 1 e Conjunto 3 possuem os mesmos elementos e são o mesmo objeto alocado em memória")

if (dq2 == c3) and (id(dq2) == id(c3)):
    print("Conjunto 2 e Conjunto 3 possuem os mesmos elementos e são o mesmo objeto alocado em memória")

if (dq1 == dq2) and (id(dq1) != id(dq2)):
    print("Conjunto 1 e Conjunto 2 possuem os mesmos elementos, porém são objetos diferentes alocados em memória")

if (dq1 == c3) and (id(dq1) != id(c3)):
    print("Conjunto 1 e Conjunto 3 possuem os mesmos elementos, porém são objetos diferentes alocados em memória")

if (dq2 == c3) and (id(dq2) != id(c3)):
    print("Conjunto 2 e Conjunto 3 possuem os mesmos elementos, porém são objetos diferentes alocados em memória")