numero1 = float(input('Insira um número: '))
numero2 = float(input('Insira outro número: '))
if numero1 > numero2:
    print('{} é maior que {}'.format(numero1, numero2))
elif numero2 > numero1:
    print('{} é maior que {}'.format(numero2, numero1))
else:
    print('Os dois número são iguais.')
