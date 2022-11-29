# Extrair elementos de forma mais eficiente do que list comprehension

frutas = ["maça", "banana", "laranja", "abacate", "pêssego"]

from operator import itemgetter

n_criticas = list(itemgetter(1, 3)(frutas))

print(n_criticas)