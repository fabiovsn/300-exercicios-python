# Retorna tipos de dados de lista

lista = [
    (1,),
    [1, 2, 3],
    (1),
    {4,5},
    {"nome":"A", "value": 2},
    10,
    [],
    1 + 3j,
    1.2,
    True,
    False,
    None,
    'Hello World'
]

for elemento in lista:
    print(elemento, type(elemento))