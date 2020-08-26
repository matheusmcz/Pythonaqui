# import bebidas
# from doce import pudim
#import math
#ceil: arredonda pra cima
#floor: arredonda para baixo
#trunc: elimina um numero
#pow: potencia
#sqrt: calcular raiz quadrada
#factorial: calculo fatorial
print('-' *5, 'UTILIZANDO MODULOS', '-' *5)
import math
number = int(input('Insira um numero: '))
raiz = math.sqrt(number)
print('Raiz quadrada de {}, é igual a: {:.2f}'.format(number, (raiz)))

print('-' *5, 'UTILIZANDO MODULOS/2', '-' *5)
from math import sqrt
number2 = int(input('Insira um numero: '))
raiz = sqrt(number2)
print('Raiz quadrada de {}, é igual a {:.2f}.'.format(number2, raiz))
