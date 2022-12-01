# Retorna o caminho de uma pasta

import os

os.mkdir("Imagens")
os.chdir("Imagens")

caminho = os.getcwd()

print(caminho)