"""
Crie um programa que leia o nome de uma cidade e diga se ela começou ou não com o
nome "SANTO".
"""
cidade = str(input('Em que cidade você nasceu? ').strip().upper())

verificacao = cidade[:5] in 'SANTO'

print(f'O nome da cidade começa com Santo? {verificacao}')
