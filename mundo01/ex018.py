from math import cos,sin, tan, radians
angulo = int(input('Qual o angulo? '))
radiano = radians(angulo)
seno = sin(radiano)
cosseno = cos(radiano)
tangente = tan(radiano)

print(f'O angulo {angulo}° tem o valor,\n Seno = {seno:.2f}\n Cosseno = {cosseno:.2f} \n Tangente = {tangente:.2f}')
