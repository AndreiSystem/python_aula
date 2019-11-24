#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e a raíz quadrada.
v = int(input("Digite um número: "));
#dobro
d = v*2;

#triplo
t = v*3;
#raíz
r = v**(1/2);


print(f'A raíz de {v} é igual à {r:.2f};');
print(f'O dobro de {v} é igual à {d};\nO triplo de {v} é igual à {t}.');

