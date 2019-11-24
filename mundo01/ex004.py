#mostra o tipo do valor
#indica todas as informações possíveis sobre ele
v = input('Digite um valor: ');
print('Qual o tipo primitivo desse valor: ', type(v));
print(f'{v} é composto só por números? ', v.isalnum());
print(f'{v} é composto só por letras? ', v.isalpha());
print(f'{v} é composto só por letras maiúsculas? ', v.isupper());
print(f'{v} é composto por letras ou números?', v.isalnum());
print(f'{v} é composto só por letras minúsculas? ', v.islower());
print(f'{v} é composto somente por espaços?', v.isspace());
print(f'{v} é composto por decimal ', v.isdecimal());

