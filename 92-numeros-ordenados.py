# Retorna lista com números ordenados

numeros = input("Digite os números separados por vírgula:\n")

lista = numeros.split(",")
lista.sort()

print(lista)