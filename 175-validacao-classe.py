# Validação de classe

import numbers

class Menu:
    def __init__(self, n):
        if isinstance(n, numbers.Number) and n > 0:
            self.n = n

        else:
            raise TypeError("Valor deve ser numérico e maior que zero")

maquina1 = Menu(5)

maquina2 = Menu('cinco')