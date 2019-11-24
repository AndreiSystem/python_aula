"""
Faça um programa que leia uma frase pelo teclado e mostre:
1- Quantas vezes aparece a letra 'A'
2- Em que posição ela aparece a primeira vez
3- Em que posição ela aparece a última vez
"""
frase = str(input('Digite uma frase: ').strip().lower())
print(frase)


qntd = frase.count('a')
print(f"""Analisando a sua frase...
A letra A aparece: {qntd}x
A primeira posição que a letra A aparece é: {frase.find('a') + 1}
A posição que a letra A aparece pela ultima vez é: {frase.rfind('a') + 1}""")