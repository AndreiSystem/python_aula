#Um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la.
#Sabendo que cada litro de tinta pinta uma área de 2m².
largura = float(input('Digite a largura da parede: '));
altura = float(input('Digite a altura da parede: '));

parede = largura * altura;
litros = parede / 2;
print(f'Para pintar {parede:.1f}m² você vai precisar de {litros:.1f}l de tinta.');