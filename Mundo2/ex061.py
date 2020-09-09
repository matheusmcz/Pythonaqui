numero = int(input('Insira o inicio: '))
razao = int(input('Insira a razão: '))
termo = numero
c = 1
while c <= 10:

    print('{} '.format(termo), end='')
    print('- ' if c < 10 else '= PAUSA', end='')
    termo = termo + razao
    c = c + 1
