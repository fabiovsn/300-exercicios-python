# Carrinho de compras com list comprehension

carrinho = []

carrinho.append(("Item 1", 30))
carrinho.append(("Item 2", 45))
carrinho.append(("Item 3", 22))
carrinho.append(("Item 4", 93))
carrinho.append(("Item 5", 6))

total = 0

for produto in carrinho:
    total = total + produto[1]

print(f"O valor total é: R$ {total}")

# Código otimizado

total2 = sum([y for x, y in carrinho])

print(f"O total é: R$ {total2}")