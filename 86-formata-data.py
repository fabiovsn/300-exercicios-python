# Formata data

import datetime

agora = datetime.datetime.now()

print("Data e hora atual:")
print(agora.strftime("%d-%m-%Y, %H:%M:%S"))