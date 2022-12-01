# Gerar nova base com dados válidos

base = ["1001", "1002", "1003", "1004", "1005", "1006", None, "1008", "1009"]
lista = []
inv = 0

for i in base:
    if i is not None:
        lista.append(i)
    else:
        inv = base.index(None)

print(f"Nova lista: {lista}")
print(f"Existe um dado inválido no índice {inv} da lista original")