# Criar pastas

import os

if not os.path.exists("backups"):
    os.mkdir("backups")

    dir = [f"mês_{str(i).zfill(2)}" for i in range(1, 13)] #zfill preenche com zeros à esquerda

    for i in dir:
        path = os.path.join("backups", i)
        os.mkdir(path)

    print(sorted(os.listdir("backups")))
else:
    print("Pasta já existente")