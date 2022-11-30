# Retorna item mais caro e mais barato

lista_compras = [{"nome":"feijão", "preco":9.79},
                 {"nome":"arroz", "preco":4.45},
                 {"nome":"carne", "preco": 20.93},
                 {"nome":"macarrão", "preco": 2.99}]

soma = sum([produto["preco"] for produto in lista_compras])

print(f"A cesta de produtos custa R$ {soma:.2f}")

produto_max = max(lista_compras, key = lambda produto:produto["preco"])
produto_min = min(lista_compras, key = lambda produto:produto["preco"])

print(f"O produto mais caro é: {produto_max['nome'].title()} - R$ {produto_max['preco']:.2f}")
print(f"O produto mais barato é: {produto_min['nome'].title()} - R$ {produto_min['preco']:.2f}")