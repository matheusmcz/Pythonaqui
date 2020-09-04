numero = int(input('DIGITE UM NÚMERO: '))
contador = 0
for c in range(1, numero + 1):
    print('{} '.format(c), end='')
    if numero % c == 0:
        contador = contador + 1
print('\nO número {} é divisivel {} vezes.'.format(numero, contador))
if contador == 2:
    print('{} É PRIMO.'.format(numero))
else:
    print('{} NÃO É PRIMO.'.format(numero))