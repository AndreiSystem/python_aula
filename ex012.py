#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço.
#Considere 5% de desconto.

produto =  float(input('Digite o preço do produto: '));

desconto = produto - (5*produto / 100);

print(f'Você deve pagar de R${produto:.2f} com 5% de desconto, apenas R${desconto:.2f}. Obrigado e volte sempre!');