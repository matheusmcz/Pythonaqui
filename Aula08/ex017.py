print('-' *5, 'TEOREMA DE PITAGORAS', '-' *5)
from math import pow
number1 = float(input('Cateto oposto: '))
number2 = float(input('Cateto adjacente: '))
hipotenuza = pow(number1, 2) + pow (number2, 2)
print ('Hipotenuza = {}' .format(hipotenuza))
