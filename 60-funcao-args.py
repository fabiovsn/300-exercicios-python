# Função com uso do *args

def mensagem(*args):
    print(f"Os parâmetros são: {args}")

ex2 = mensagem("nome=Fernando", "idade=33", "profissão=professor")