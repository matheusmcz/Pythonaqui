print('{:-^40}'.format('TABUADA!'))

while True:
    numero = int(input('Número da tabuada: '))
    if numero < 0:
        break
    for c in range(1, 11):
        print(f'{numero} x {c} = {numero * c}')

print('TABUADA FINALIZADA.')
