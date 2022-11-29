# texto = input("Digite um texto:\n")
#
# maiusculas = []
# minusculas = []
#
# for letra in texto:
#     if letra.islower():
#         minusculas.append(letra)
#     elif letra.isupper():
#         maiusculas.append(letra)
#
# print(f"No texto {texto} foram encontradas as seguintes letras maiúsculas: {maiusculas}")
# print(f"No texto {texto} foram encontradas {len(maiusculas)} as seguintes letras maiúsculas")
#
# print(f"No texto {texto} foram encontradas as seguintes letras minúsculas: {minusculas}")
# print(f"No texto {texto} foram encontradas {len(minusculas)} as seguintes letras minúsculas")

# Método reduzido

texto = input("Digite o texto:\n")

minusculas = [letra for letra in texto if letra.islower()]
maiusculas = [letra for letra in texto if letra.isupper()]

print(f"No texto {texto} foram encontradas as seguintes letras maiúsculas: {maiusculas}")
print(f"No texto {texto} foram encontradas {len(maiusculas)} as seguintes letras maiúsculas")
print(f"No texto {texto} foram encontradas as seguintes letras minúsculas: {minusculas}")
print(f"No texto {texto} foram encontradas {len(minusculas)} as seguintes letras minúsculas")