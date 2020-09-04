numero = int(input('Insira um número: '))
print('''BASES DE CONVERSÃO:
[ 0 ] BINÁRIO
[ 1 ] OCTAL
[ 2 ] HEXADECIMAL
''')
escolha = int(input('SUA OPÇÃO: '))
if escolha == 0:
    print('\n{} em BINÁRIO = {}'.format(numero, bin(numero)[2:]))
if escolha == 1:
    print('\n{} em OCTAL = {}'.format(numero, bin(numero)[2:]))
if escolha == 2:
    print('\n{} em HEXADECIMAL = {}'.format(numero, hex(numero)[2:]))
