print('{:=^40}'.format(' PROGRESSÃO ARITMETICA '))
termo = int(input('INSIRA O TERMO: '))
razao = int(input('RAZÃO DE PROGRESSÃO: '))
soma = 0
for c in range(1, 11):
    soma = soma + razao
    print('{} ==>'.format(soma), end=' ')
print('FIM')
