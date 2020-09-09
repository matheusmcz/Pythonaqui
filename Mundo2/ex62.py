numero = int(input('Insira o inicio: '))
razao = int(input('Insira a razão: '))
termo = numero
c = 1
total = 0
continua = 10
while continua != 0:
    total = total + continua
    while c <= total:
        print('{}- '.format(termo), end='')
        termo = termo + razao
        c = c + 1
    print('PAUSA')
    continua = int(input('\nDeseja continuar? '))
print('FIM')
