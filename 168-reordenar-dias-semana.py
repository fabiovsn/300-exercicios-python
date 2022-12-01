# Reordenar dias da semana

from collections import deque

semana = deque(["Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo", "Segunda"])
semana.rotate(1)

print(semana)