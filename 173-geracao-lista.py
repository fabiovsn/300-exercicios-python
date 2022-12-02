# Geração de lista

import random

random.seed(32)

linguagens = ["python", "java", "php", "c++", "c#", "javascript", "kotlin", "r"]
random.shuffle(linguagens)
print(linguagens)

random.seed(42)

random.shuffle(linguagens)
print(linguagens)