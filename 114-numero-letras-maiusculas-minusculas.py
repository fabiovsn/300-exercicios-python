# Retornar número de letras maiúsculas e minúsculas

texto = input("Digite um texto:\n")
maiusculas = 0
minusculas = 0

for letra in texto:
    if(letra.islower()):
        minusculas += 1
    if(letra.isupper()):
        maiusculas += 1

print(f"No texto '{texto}' foram encontradas {maiusculas} letras maiúsculas")
print(f"No texto '{texto}' foram encontradas {minusculas} letras minúsculas")