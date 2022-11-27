# Formatação de estilo

def negrito(palavra):
    def transforma():
        return "<b>" + palavra() +"</b>"
    return transforma

def italico(palavra):
    def transforma():
        return "<i>" + palavra() +"</i>"
    return transforma

def sublinhado(palavra):
    def transforma():
        return "<u>" +palavra()+"</u>"
    return transforma

@negrito
@italico
@sublinhado

def aplica_estilo():
    palavra = input("Digite uma palavra\n")
    return palavra

print(aplica_estilo())
