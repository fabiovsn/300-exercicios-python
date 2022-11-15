# Contagem primos

numero = int(input("Digite o número:\n"))
divisoes = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        print(i)
        divisoes += 1

if divisoes == 2:
    print(f"O número {numero} é primo")
    print(f"O númer {numero} é divisível apenas por 1 e por {numero}")
else:
    print(f"O número {numero} não é primo")
    print(f"O número {numero} é divisível {divisoes} vezes")