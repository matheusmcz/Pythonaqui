numero = int(input('Insira um número: '))
resto = numero % 2
if resto == 0:
    print('O número {} é PAR!'.format(numero))
else:
    print('O número {} é IMPAR.'.format(numero))
