"""
Crie um programa que leia o nome de uma pessoa e diga se ela "SILVA" no nome.
"""
nome = str(input('Digite seu nome: ').strip().upper())
verificacao = 'SILVA' in nome
print(f'Possuí Silva no seu nome? {verificacao}')
