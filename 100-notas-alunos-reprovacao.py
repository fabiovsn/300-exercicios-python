# Verifica se o aluno etá de recuperação

def calcula_nota(nota):
    if nota < 0 or nota > 1:
        print("Pontuação inválida!!!")
        print("A nota deve ser uma pontuação entre 0 e 1")
    elif nota == 1.0:
        print("Parabéns, você gabaritou a prova!!")
    elif nota >= 0.6:
        print("Parabéns, você foi aprovado!!!")
    elif nota < 0.6:
        print("Nota abaixo da média, você está em recuperação!!!")
    else:
        print("Não foi possível computar sua nota!!!")

try:
    nota = float(input("Digite uma nota:\n"))
except:
    print("Valor inválido!!!")
    print("Use somente números com casas decimais entre 0 e 1.0")
    quit()

calcula_nota(nota)