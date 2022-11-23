# Recebe string e retorna string convertida em maiúscula

class Conversor(object):
    def __init__(self):
        self.s = ""

    def recebe_string(self):
        self.s = input("Digite uma palavra/frase:\n")

    def exibe_string(self):
        print(self.s.upper())

frase1 = Conversor()

frase1.recebe_string()
frase1.exibe_string()