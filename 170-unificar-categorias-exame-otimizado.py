# Unificar categorias de exames

from collections import defaultdict

data = [
            ("Raios-X", "Raios-X"),
            ("Magnetismo", "Ressonância Magnética"),
            ("Ultrassom", "Ecografia"),
            ("Medicina Nuclear", "Cintilografia"),
            ("Raios X", "Tomografia Computadorizada"),
            ("Medicina Nuclear", "PET-CT"),
            ("Raios-X", "Mamografia"),
            ("Raios-X", "Densiometria Óssea"),
        ]

def_dict = defaultdict(list)
for i, j in data:
    def_dict[i].append(j)

print(def_dict)