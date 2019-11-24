"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
o primeiro e o último nome separadamente
ex: Ana Maria de Souza
primeiro = Ana
último = Souza
"""

n = str(input('Digite seu nome completo: ').strip())
nome = n.split()

print(f"""Analisando o seu nome...
O seu Primeiro nome é {nome[0]}
O seu Último nome é {nome[len(nome)-1]}""")

