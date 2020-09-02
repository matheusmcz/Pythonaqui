velocidadecarro = int(input('Qual velocidade do carro em KM/h? '))

if velocidadecarro > 80:
    print('Você foi muito rápido!!')
    print('\nMulta por excessso de velocidade: R${}'.format((velocidadecarro - 80) * 7.0))
else:
    print('Você respeitou o limite de velocidade!')
