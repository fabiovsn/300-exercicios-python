# Canal de cor zero

import numpy as np

import numpy as np

imagem = np.random.randint(low=0,
                           high=256,
                           size=(10, 10, 3),
                           dtype=np.uint8)

print(imagem[:, :, 0])