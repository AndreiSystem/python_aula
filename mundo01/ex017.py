"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
triângulo retângulo, calcule e mostre o comprimento da hipotenusa
"""
from math import hypot

c_oposto = float(input('Comprimento do cateto oposto: '))
c_adjacente = float(input(('Comprimento do cateto adjacente: ')))

#hypot() -> calcula a hipotenusa
hi = hypot(c_oposto, c_adjacente)




print(f'A hipotenusa vai medir {hi:.2f}')