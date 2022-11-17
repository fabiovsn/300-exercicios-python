# Função que retorna mensagem de boas vindas com nome

def mensagem(nome):
    print(f"Bem vindo(a) {nome}")

nome = input("Digite o seu nome:\n")
nome = mensagem(nome)