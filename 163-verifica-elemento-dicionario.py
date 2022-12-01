# Verifica se elemento já existe em dicionário

clientes = {"Fernando":"991357259", "Alberto":"981120491"}

novo_cliente = input("Digite o nome do cliente:\n")

if novo_cliente in clientes.keys():
    print(f"{novo_cliente} já existe na base de dados")
    novo_cliente = input("Digite o nome do cliente:\n")
if novo_cliente not in clientes.keys():
    print(f"Para inserir {novo_cliente} na base de dados, digite um telefone:\n")
    clientes.__setitem__(novo_cliente, str(input("Digite o telefone:\n")))

print(clientes)