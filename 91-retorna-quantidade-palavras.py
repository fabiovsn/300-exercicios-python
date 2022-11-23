# Retorna quantidade de palavras em uma frase

frequencia = {}

texto = "Se alguma coisa pode dar errado, dará errado, e mais: dará" \
        "errado da pior maneira possível, no pior momento possível e de " \
        "modo que causa o maior dano possível"

for palavra in texto.split():
    frequencia[palavra] = frequencia.get(palavra, 0) + 1

palavras = frequencia.keys()

for i in palavras:
    print(f"{i} = {frequencia[i]}")