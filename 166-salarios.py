# Salários funcionários

from collections import namedtuple

funcionario = namedtuple("ID", "Cargo Detalhes")
funcionarios = []

func001 = funcionario("Gerente", {"Nome":"Anna","Salário":"R$2750,95"})
func002 = funcionario("Fiscal", {"Nome":"Carlos Santos","Salário":"R$2480,00"})
func003 = funcionario("Fiscal", {"Nome":"Carlos Silva","Salário":"R$2190,00"})

print(f"{func001}\n{func002}\n{func003}")

funcionarios.append(func001)
funcionarios.append(func002)
funcionarios.append(func003)

print(funcionarios)