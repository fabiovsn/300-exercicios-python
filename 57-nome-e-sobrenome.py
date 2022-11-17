# Recebe nome e sobrenome e imprime mensagem

def boas_vindas(nome, sobrenome):
    print(f"Bem vindo(a) {nome} {sobrenome}")

nome = input("Digite o seu nome:\n")
sobrenome = input("Digite o seu sobrenome:\n")

pessoa = boas_vindas(nome, sobrenome)