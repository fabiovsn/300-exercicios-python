# Identificar maior número entre três

x = int(input("Digite o primeiro número:\n"))
y = int(input("Digite o segundo número:\n"))
z = int(input("Digite o terceiro número:\n"))

def maior_de_dois(x, y):
    if x > y:
        return x
    return y

def maior_de_tres(x, y, z):
    return maior_de_dois(x, maior_de_dois(y, z))

print(f"O maior número entre {x}, {y} e {z} é: {maior_de_tres(x, y, z)}")