print('-' *5, 'SEN, COS, TANG', '-' *5)

from math import sin, cos, tan, radians
angulo = float(input('Insira o ângulo: '))
anguloRadiano = radians(angulo)
sen = sin(anguloRadiano)
cos = cos(anguloRadiano)
tg = tan(anguloRadiano)
print('Valor do Seno = {:.2f}\nValor do Coseno = {:.2f}\nValor da Tangente = {:.2f}'.format(sen, cos, tg))
