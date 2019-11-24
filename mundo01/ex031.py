"""
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
e R$0.45 para viagens mais longas.
"""
distancia = float(input('Digite a distância da viagem em Km: '))
print(f'Viagem de {distancia:.1f}Km.')

if distancia <= 200:
    valor = distancia * 0.50
    print(f'Preço da passagem de R${valor:.2f}')
else:
    valor = distancia * 0.45
    print(f'Preço da passagem de R${valor:.2f}')

print('\033[32mBoa viagem!\033[m')
