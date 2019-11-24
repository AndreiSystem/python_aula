#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

medida = int(input('Digite o valor do metro para ser convertido: '));

km = medida / 1000;
hm = medida / 100;
dam = medida / 10;
dm = medida * 10;
cm = medida * 100;
mm = medida * 1000;


print(f'{medida} metros == {mm} mm;\n{medida} metros == {cm} cm;');
print(f'{medida} metros == {dm} dm;\n{medida} metros == {dam} dam;');
print(f'{medida} metros == {hm} hm;\n{medida} metros == {km} km.');