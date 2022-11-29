# Verifica se endereço de site foi digitado corretamente

running = True

while running:

    endereco = input("Digite o endereço do site:\n")
    if (endereco.startswith("www.") and endereco.endswith(".com.br"))!=True:
        print("O endereço deve incluir 'www' e '.com.br' ")
    else:
        running = False

print(f"{endereco} é um endereço válido!")