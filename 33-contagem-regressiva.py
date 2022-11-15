# Contagem regressiva de 20 segundos

from time import sleep

for i in range(0, 20 + 1):
    print(i)
    sleep(1)
print("Contagem terminada")
