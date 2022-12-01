# Unificar categorias de exames

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

data_dict = {}
for i, j in data:
    data_dict.setdefault(i, []).append(j)

print(data_dict)