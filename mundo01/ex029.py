"""
Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar 80km/h. Mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7.00 por cada km acima do limite.
"""
velocidade = int(input('Digite a velocidade do carro: '))
multa = (velocidade - 80) * 7

if velocidade > 80:
    print(f"""\033[31mMULTADO! Você excedeu o limite permitido que é de 80Km/h
Você deve pagar uma multa de\033[m \033[33mR${multa:.2f}!\033[m""")

print('\033[32mTenha um bom dia! Dirija com segurança!\033[m')

