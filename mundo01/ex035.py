"""
Leia o comprimento de três retas e diga ao usuário se eles podem ou não formar
um triângulo
"""
print('-='*20)
print('Analisador de triângulos')
print('-='*20)
c1 = float(input('Digite o primeiro comprimento: '))
c2 = float(input('Digite o segundo comprimento: '))
c3 = float(input('Digite o terceiro comprimento: '))


if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    print('PODEM formar um triângulo!')
else:
    print('NÃO PODEM formar um triângulo!')