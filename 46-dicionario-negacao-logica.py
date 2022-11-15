# Verificar se Python consta no dicionário usando negação lógica

dicionario = {"Alto nível": "Python",
              "Médio nível": "C",
              "Baixo nível": "Assembly"}

for i in dicionario.values():
    if not i == "Python":
        print("Python não consta no dicionário")
    else:
        print("Python consta no dicionário")
    break