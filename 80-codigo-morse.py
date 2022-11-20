# Recebe string e converte em código Morse

def texto_p_morse(texto):
    d = {
        "A": ".-", "B":"-...",
        "C": "-.-", "D": "-..", "E": ".",
        "F": "..-.", "G": "--.", "H": "....",
        "I": "..", "J": ".---", "K": "-.-",
        "L": ".-..", "M": "--", "N": "-.",
        "O": "---", "P": ".--.", "Q": "--.-",
        "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--",
        "X": "-..-", "Y": "-.--", "Z": "--..",
        "1": ".----", "2": "..---", "3": "...--",
        "4": "....-", "5": ".....", "6": "-....",
        "7": "--...", "8": "---..", "9": "----.",
        "0": "-----", ",": "--..--", ".": ".-.-.-",
        "?": "..--..", "/": "-..-.", "-": "-....-",
        "(": "-.--.", ")": "-.--.-", "!": "-.-.--",
        "": "", "''": ".----.", ":": "---..."
    }

    return "".join(d[i] for i in texto.upper())

texto = input("Digite o texto a ser convertido para código Morse:\n")
conversor = texto_p_morse(texto)

print(f"{texto} em Código Morse: {conversor}")

