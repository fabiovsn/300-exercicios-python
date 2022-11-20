# Recebe um número e retorna as duas metades

def divide_pela_metade(num):
    return [num//2, num-num//2]

num = int(input("Digite um número:\n"))
print(divide_pela_metade(num))