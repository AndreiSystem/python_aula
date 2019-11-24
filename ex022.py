"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
1- O nome com todas as letras maiúsculas.
2- O nome com todas minúsculas.
3- Quantas letras ao todo(sem considerar espaços).
4- Quantas letras tem o primeiro nome.
"""

nome = str(input('Digite o seu nome completo: '))

maiusculas = nome.upper()
minusculas = nome.lower()
qnt_letras = len(nome.replace(' ', ''))
letras_primeiro = nome.split()


print(f"""Seu nome [ {nome} ] tem as seguintes informações...

Com todas as letras maiúsculas: {maiusculas}
Com todas as letras minúsculas: {minusculas}
Quantas letras ao todo: {qnt_letras}
Quantas letras tem o seu primeiro nome: {len(letras_primeiro[0])}""")