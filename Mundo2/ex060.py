'''from math import factorial
print('{:=^40}'.format('Calculo Fatorial.'))
numero = int(input('Informe um número: '))
f = factorial(numero)
print('O fatorial do número informado foi {} = {}'.format(numero, f))'''

numero = int(input('Calculo Fatorial: '))
c = numero
f = 1
print('Calculando {}! = '.format(numero), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c = c - 1
print('{}'.format(f))
