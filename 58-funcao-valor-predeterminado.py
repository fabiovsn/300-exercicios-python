# Função com dois parâmetros, sendo um com valor determinado

def boas_vindas(nome, nacionalidade="Brasileiro(a)"):
    print(f"{nome} é {nacionalidade}")

nome = input("Digite o seu nome:\n")

ex1 = boas_vindas(nome)

nacionalidade = input("Digite sua nacionalidade:\n")
ex2 = boas_vindas(nome, nacionalidade)