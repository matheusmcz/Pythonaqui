numero1 = float(input('Insira o primeiro número: '))
numero2 = float(input('Insira o segundo número: '))
numero3 = float(input('Insira o terceiro número: '))
# lista = (numero1, numero2, numero3)
if numero1 < numero2 and numero1 < numero3:
    print('O menor número é {:.2f}.'.format(numero1))
elif numero2 < numero1 and numero2 < numero3:
    print('O menor número é {:.2f}.'.format(numero2))
elif numero3 < numero1 and numero3 < numero2:
    print('O menor número é {:.2f}.'.format(numero3))
if numero1 > numero2 and numero1 > numero3:
    print('O maior número é {:.2f}.'.format(numero1))
elif numero2 > numero1 and numero2 > numero3:
    print('O maior número é {:.2f}.'.format(numero2))
elif numero3 > numero1 and numero3 > numero2:
    print('O maior número é {:.2f}.'.format(numero3))
