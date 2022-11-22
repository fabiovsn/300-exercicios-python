# Gera senha aleatória com tamanho definido pelo usuário

import random

tamanho = int(input("Enter the length of password:\n"))

s = "abcdefghijklmnopkrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

senha = "".join(random.sample(s, tamanho))

print(senha)