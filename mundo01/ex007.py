#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a média.

n1 = float(input('Digite a primeira nota: '));
n2 = float(input('Digite a segunda nota: '));

m = (n1 + n2) / 2;

print(f'A média atingida pelo aluno foi de {m:.2f}');