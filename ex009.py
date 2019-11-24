#Faça um programa que leia um número Inteiro qualquer e mostre na tela a tabuada.

n = int(input('Digite um número: '));

x = 1;
print('-'*15)
while ( x <= 10) :
    print(f'{n} x {x} = {n*x}')
    x = x + 1;
print('-'*15)