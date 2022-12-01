# Retorna número por extenso

def conversor(num):
    match num:
        case 0:
            return "Zero"
        case 1:
            return "Um"
        case 2:
            return "Dois"
        case 3:
            return "Três"
        case 4:
            return "Quatro"
        case 5:
            return "Cinco"

numero = int(input("Digite um número de 0 a 5:\n"))
print(conversor(numero))