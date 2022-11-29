from dataclasses import dataclass

@dataclass(frozen=True)
class Cachorro:
    cor: str
    idade: int

pet1 = Cachorro("Preto e Branco", 6)
print(pet1.cor)