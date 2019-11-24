""""
**import math importa toda a biblioteca de matemática
import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print(f'A raíz de {num} é igual a {raiz:.2f} e se arrendoda-la resulta em {math.ceil(raiz)}')

#from math import importa somente um módulo especifico
from math import sqrt

num = int(input('Digite um número: '))
raiz = sqrt(num)

print(raiz)

#caso queira consultar mais bibliotecas é só acessar python.org/docs
"""

import random

num = random.randint(1, 10)
print(num)