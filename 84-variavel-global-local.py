# Exibir conteúdo de variável global e local

def msg():
    global mensagem
    print(mensagem)
    mensagem = "Usufrua das funcionalidades do sistema"
    print(mensagem)

mensagem = "Olá, seja bem vindo(a)"

msg()
