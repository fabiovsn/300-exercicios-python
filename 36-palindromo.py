# # Palíndromo
#
# frase = str(input("Digite uma palavra ou frase\n")).strip().upper()
# palavras = frase.split()
# caracteres = "".join(palavras)
# fraseinvertida = ""
#
# for i in range(len(caracteres)-1, -1, -1):
#     fraseinvertida += caracteres[i]
#
# print(caracteres, fraseinvertida)
#
# if fraseinvertida == caracteres:
#     print("É um palíndromo")
# else:
#     print("Não é um palíndromo")

# alternativa

frase = input("Digite uma palavra ou frase\n").strip().upper().replace(" ", "")
print(frase)
frase_invertida = ""
for i in range(len(frase) -1, -1, -1):
    frase_invertida += frase[i]

if frase == frase_invertida:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")