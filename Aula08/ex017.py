print('-' *5, 'TEOREMA DE PITAGORAS', '-' *5)
from math import pow, hypot
number1 = float(input('Cateto oposto: '))
number2 = float(input('Cateto adjacente: '))
hipotenuza =(pow(number1, 2) + pow (number2, 2))**(1/2)
print ('Hipotenuza = {:.2f}' .format(hipotenuza))


n = float(input('Cateto oposto: '))
n1 = float(input('Cateto adjacente: '))
hi = hypot(n, n1)
print('Hipotenuza = {:.2f}'.format(hi))
