# Formas de retornar soma

x = [10, 12, 35]

# Método 1

num = x[0] + x[1] + x[2]
print(num)

# Método 2

num = sum([i for i in x])
print(num)

# Método 3

num = sum(x)
print(num)

# Método 4

def soma(x):
    total = 0
    for i in x:
        total += i
    print(total)

num = soma(x)

# Método 5

n1, n2, n3 = x
num = n1 + n2 + n3
print(num)