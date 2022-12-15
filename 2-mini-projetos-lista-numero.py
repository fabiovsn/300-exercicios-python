# def valida_lista(lista):
#     for i in range(0, len(lista)):
#         if lista[i] < 0 or lista[i] > 99:
#             return False
#         else:
#             return True
#
# lista_valores = []
# while len(lista_valores) != 5:
#
#     valores = input("Digite 5 números entre 0 e 99 separados por vírgula.\n")
#
#     lista_valores = valores.split(',')
#     lista_convertida = [int(x) for x in lista_valores]
#     if len(lista_convertida) == 5:
#         retorno = valida_lista(lista_convertida)
#         if retorno:
#             print('Lista válida.')
#             tupla_valores = tuple(lista_convertida)
#             print(lista_convertida)
#             print(tupla_valores)
#         else:
#             print('Lista inválida. Há valores menores que zero ou maiores que 99.')

# versão orientada a objetos

class ListaTupla(object):
    def __init__(self):
        self.valores = input('Digite 5 números entre 0 e 99, separados por vírgula:\n')
        self.lista_valores = self.valores.split(',')
        self.lista_valores = [int(i) for i in self.lista_valores]

        def val_tamanho(lista_valores):
            if len(self.lista_valores) != 5:
                print('Você deve digitar 5 números.')
                return False
            return True

        def val_valor(lista_valores):
            for i in range(0, len(self.lista_valores)):
                if self.lista_valores[i] < 0 or self.lista_valores[i] > 99:
                    print('Existem valores acima de 99 ou abaixo de 0 na lista')
                    return False
                return True

        while val_tamanho(self.lista_valores) and val_valor(self.lista_valores) == True:
            self.tupla_valores = tuple(self.lista_valores)
            print('Valores válidos!')
            print(self.lista_valores)
            print(self.tupla_valores)
            break

var1 = ListaTupla()