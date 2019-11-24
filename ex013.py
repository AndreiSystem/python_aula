#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário.
#com 15% de aumento.

salario = float(input('Digite o salário do funcionário: '));
aumento = salario + (salario * 15 / 100);

print(f'O salário final do funcionário será de R${aumento:.2f} com os 15% de aumento.')