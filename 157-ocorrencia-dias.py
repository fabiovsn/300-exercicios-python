# Número de ocorrências de determinado dia

from datetime import datetime

segundas = 0
meses = range(1, 12 + 1)

ano_inicio = int(input("Digite o ano inicial: "))
ano_fim = int(input("Digite o ano final: "))

intervalo = []
intervalo.append(ano_inicio)
intervalo.append(ano_fim)

for ano in range(intervalo[0], intervalo[1] + 1):
    for mes in meses:
        if datetime(ano, mes, 1).weekday() == 0:
            segundas += 1

print(f"Entre {intervalo[0]} e {intervalo[1]} existem {segundas} segundas-feiras no primeiro dia do mês")