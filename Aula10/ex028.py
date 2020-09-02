import random

print('-' * 5, 'ADIVINHAÇÃO', '-' * 5)
sorteio = random.randint(0, 5)
print('\n\nVou escolher um número de 0 a 5... \nTente advinhar qual eu pensei okay?')
number = int(input('\nEm que número eu pensei?'))
if number != sorteio:
    print('ERROU!! Eu escolhi {}'.format(sorteio))
else:
    print('ACERTOU!!')
