"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor
"""

"""
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))

menor = n1
maior = n1

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n2

print(f'O menor valor é {menor}')
print(f'O maior valor é {maior}')
"""

#Usando metódo com lista

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))

lista = [n1, n2, n3]

maior = max(lista)
menor = min(lista)

print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')

