clientes = {"Fernando":"991357259", "Alberto": "981120491"}


running = True

while running:
    novo_cliente = input("Digite o nome do cliente:\n")
    if novo_cliente in clientes.keys():
        print(f"{novo_cliente} já existe na base de dados")
    else:
        telefone = str(input("Digite o telefone:\n"))
        clientes.__setitem__(novo_cliente, telefone)
        running = False

print(clientes)