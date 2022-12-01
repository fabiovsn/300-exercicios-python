# Conversão texto para notação numérica computacional

def conv_bytes(bytes):
    sufixo = "B"

    for i in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if abs(bytes) < 1024.0:
            return "%3.1f%s%s" % (bytes, i, sufixo)
        bytes /= 1024.0
    return "%.1f%s%s" % (bytes, "Y", sufixo)

num = int(input("Digite um número:\n"))
numc = conv_bytes(num)

print(numc)