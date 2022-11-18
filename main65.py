# Exercício 65 - consultas médicas com usuário cadastrado
import medicos
import medicos65
import cadastro_plano_saude65

usuario = str(input("Digite seu número de usuário:\n"))
if usuario in cadastro_plano_saude65.usuarios.keys():
    if usuario == "001":
        usuario = "Fernando"
        print("Bem vindo, Fernando")

    elif usuario == "002":
        usuario = "Ana Clara"
        print("Bem vinda Ana Clara")
    else:
        print("Usuário desconhecido ou não cadastrado.")

    menu = str(input("Deseja agendar uma consulta? (S ou N)\n")).upper()
    if menu == "S":
        print("Escolha com qual médico deseja consultar:")
        print("1 - Graziela Veiga")
        print("2 - Matheus Correa")

        medico = int(input("Com qual médico deseja agendar consulta?\n"))
        if medico == 1:
            print(f"{usuario}, sua consulta com a Dra. {medicos.medicos[0]} está agendada!")
        elif medico == 2:
            print(f"{usuario}, sua consulta com o Dr. {medicos.medicos[1]} está agendada!")
    else:
        print("Agradecemos seu contato!")

else:
    print("Usuário não cadastrado")