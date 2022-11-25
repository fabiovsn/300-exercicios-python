# Classe Carro

class Carro:
    def __init__(self, marca=None, modelo=None, ano=None, cor=None, valor=None):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.valor = valor

    def descricao(self):
        descricao_carro = f"{self.marca}, {self.modelo}, {self.ano}, {self.cor}, {self.valor}"
        return descricao_carro

carro1 = Carro("Audi", "A3", 2006, "Preto", "R$ 19.900")
carro2 = Carro("Renault", "Megane", 2010, "Preto", "R$ 22.500")
carro3 = Carro("Chevrolet", "Cruise", 2018, "Vermelho", "R$ 49.000")

print(carro1)
print(carro2)
print(carro3)

print(carro1.descricao())
print(carro2.descricao())
print(carro3.descricao())