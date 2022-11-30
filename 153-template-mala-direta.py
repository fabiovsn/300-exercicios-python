# Template de mala direta

from string import Template

nomes = ["Anna", "Paulo", "Maria", "Rafael", "Patrícia"]

email = """ Olá $name,
Seja muito bem vindo(a) ao curso Python!!!

"""

template = Template(email)

for i in nomes:
    print(template.substitute(name=i))
    print("-" * 42)