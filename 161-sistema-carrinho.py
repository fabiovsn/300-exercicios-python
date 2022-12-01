# Carrinho de compras simples

# carrinho = []
# objeto = True
# opcao = ""
#
# while objeto:
#     opcao = int(input("Digite uma opção: 1 - Inserir; 2 - Excluir; 3-Sair\n"))
#     if opcao == 1:
#         objeto = input("Digite o nome do objeto a ser inserido:\n")
#         carrinho.append(objeto)
#         print(carrinho)
#     elif opcao == 2:
#         objeto = input("Digite o nome do objeto a ser excluído:\n")
#         if objeto in carrinho:
#             carrinho.remove(objeto)
#             print("Objeto excluído com sucesso!")
#         else:
#             print("Objeto não existe no carrinho")
#         print(carrinho)
#     elif opcao == 3:
#         print("Obrigado por comprar conosco!\n")
#         objeto = False
#     else:
#         print("Opção inválida!")

# alternativa

carrinho = []

print("Digite o nome e pressione ENTER para inserir no carrinho.")
print("Digite CORRIGE para remover o último item inserido.")
print("Digite SAIR para fechar o carrinho de compras")

while (obj:=input("Digite um objeto:\n"))!="sair":
    carrinho.append(obj); print(carrinho)

    if obj == "corrige":
        del(carrinho[-2]); del(carrinho[-1]); print(carrinho)

print(f"Listas de compras final:\n{carrinho}")
