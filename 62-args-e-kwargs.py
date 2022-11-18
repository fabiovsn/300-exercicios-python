#Uso do args e kwargs

def identificador(*args, **kwargs):
    for n in args:
        nome = n
        #print(f'{n}')

        for k, v in kwargs.items():
            idade = k
            sexo = v

            #print(f"{idade},{sexo}")

            print(f"Nome: {nome},{idade}, {sexo}")

pessoa = identificador('Fernando', idade=23, sexo = 'M')
