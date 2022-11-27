# Verifica se o endereço do site foi digitado corretamente

endereco = ""

while ((endereco.startswith("www.") and endereco.endswith(".com.br"))) != True:
    endereco = input("Digite o endereço do site:\n")

print(f"{endereco} é um endereço válido!")
