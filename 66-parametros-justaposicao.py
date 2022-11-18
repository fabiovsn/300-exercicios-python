# Função que recebe parâmetros por justaposição

numeros = (33, 1987, 2020)
dados = {"Nome":"Fernando", "Profissão":"Engenheiro"}

def identificador(*args, **kwargs):
    print(args)
    print(kwargs)

identificador(*numeros, **dados)

