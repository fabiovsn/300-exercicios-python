# Crie uma estrutura orientada a objetos híbrida

class Usuario:
    nome = "Usuário"
    senha = "padrao"

    def __init__(self, nome=None, senha=None):
        self.nome = nome
        self.senha = senha

usuario1 = Usuario("admin", "00237")
print(f"Usuário registrado:{Usuario.nome}")