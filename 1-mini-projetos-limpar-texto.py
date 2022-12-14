import re

texto = """
Ainda assim, existem dúvidas a respeito de como o surgimento do comércio virtual
facilita a criação do orçamento setorial.
Todas estas questões, devidamente ponderadas, levantam dúvidas sobre se a
competitividade nas transações comerciais desafia a capacidade de
equalização dos relacionamentos verticais entre as hierarquias.
O cuidado em identificar pontos críticos na consolidação das estruturas não
pode mais se dissociar dos conhecimentos estratégicos para atingir a excelência.
"""

texto = texto.replace('\n', ' ')
texto = re.sub(r'[?|$|.|!|"|,|;|:|-]', r'', texto)

lista_palavras = texto.lower().split()
# print(lista_palavras)

def dicionario_frequencia(lista):
    frequencia_palavras = [lista.count(p) for p in lista]
    return dict(list(zip(lista, frequencia_palavras)))

def ordena_dicionario_freq(dicionario):
    aux = [(dicionario[key], key) for key in dicionario]
    aux.sort()
    aux.reverse()
    return aux

dicionario_freq = dicionario_frequencia(lista_palavras)

print(ordena_dicionario_freq(dicionario_freq))
