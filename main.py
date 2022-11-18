# Exercício 64 - consultas médicas

import medicos

menu = str(input("Deseja agendar uma consulta? S ou N\n")).upper()

if menu == 'S':
    paciente = input("Por favor, digite o seu nome completo:\n")
    print(f"{paciente}, escolha com qual médico deseja consultar:\n")
    print("1 - Graziela Veiga")
    print("2 - Matheus Correa")

    medico = int(input("Com qual médico deseja agendar a consutla?\n"))
    if medico == 1:
        print(f"Sua consulta com a Dra. {medicos.medicos[0]} será agendada.")
    elif medico == 2:
        print(f"Sua consulta com o Dr. {medicos.medicos[1]} será agendada.")
    else:
        print("Agradecemos o seu contato!")

else:
    print("Obrigado pela visita!")


