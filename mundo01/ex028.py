"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre
0 a 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo
computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu
"""
from random import randint
import playsound
n_random = randint(1, 5)

resp = int(input('Digite um número de 1 à 5: '))


if resp == n_random:
    print('Acertou!')
    playsound.playsound('C:/Users/andre/Desktop/musica/Acertou.mp3')

else:
    print('ERROU!')
    playsound.playsound('C:/Users/andre/Desktop/musica/Errou.mp3')


print('Fim de jogo!')
