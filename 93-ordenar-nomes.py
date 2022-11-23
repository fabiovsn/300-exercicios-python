# Retorna lista com nomes ordenados

nomes = [x for x in input("Digite os nomes separados por vírgula:\n").split(",")]
nomes.sort()

print(",".join(nomes))