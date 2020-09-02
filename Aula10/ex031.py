print('--' * 5, 'Bem-Vindo a AEROP', '--' * 5)
distanciaviagem = int(input('\nDistância em Km da viagem: '))
print('----' * 5)
if distanciaviagem <= 200:
    print('O valor da passagem será de: R$ {}'.format(distanciaviagem * 0.50))
else:
    print('O valor da passagem será de: R$ {}'.format(distanciaviagem * 0.45))
