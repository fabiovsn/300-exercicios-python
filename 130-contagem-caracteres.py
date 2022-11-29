# Contagem de caracteres de frase

from collections import Counter

texto = "A Radiologia é a ciência que estuda a anatomia por meio de exames de imagem"

a1, a2, a3, a4, a5, a6 = Counter(texto).most_common(6)

print(a1, a2, a3, a4, a5, a6)

print(f"A letra mais recorrente é: '{a1[0]}', repetida '{a1[1]}' vezes")
print(f"A segunda letra mais recorrente é: '{a2[0]}', repetida '{a2[1]}' vezes")
print(f"A terceira letra mais recorrente é: '{a3[0]}', repetida '{a3[1]}' vezes")
print(f"A quarta letra mais recorrente é: '{a4[0]}', repetida '{a4[1]}' vezes")
print(f"A quinta letra mais recorrente é: '{a5[0]}', repetida '{a5[1]}' vezes")
print(f"A sexta letra mais recorrente é: '{a6[0]}', repetida '{a6[1]}' vezes")