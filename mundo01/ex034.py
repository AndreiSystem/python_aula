"""
Para salário superiores a R$1.250,00. Calcule um aumento de 10%
Para inferiores ou iguais, o aumento é de 15%.
"""

salario = float(input('Digite o salário do funcionário? R$'))

if salario <= 1250:
    aumento = (salario * 15 / 100) + salario
    print(f'Salário final com 15% de aumento: R${aumento:.2f}')
else:
    aumento = (salario * 10 / 100) + salario
    print(f'Salário final com 10% de aumento: R${aumento:.2f}')

