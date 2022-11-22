# Recebe nome e sobrenome e altera para padrão americano

def inverte_nome(n):
    nome, sobrenome = n.split()
    return "".join([sobrenome, " ", nome])

pessoa = input("Digite seu nome e sobrenome:\n")
pessoa = inverte_nome(pessoa)

print(pessoa)