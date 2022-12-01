# Retorna nome de arquivos, se houver

import os

ext = (".jpg", ".jpeg", ".bmp", ".png", ".gif")

arquivos = sorted([i for i in os.listdir("C:\\Users\\fabio\\Pictures\\Amgy") if i.endswith(ext)])

print(arquivos)