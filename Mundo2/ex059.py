numero1 = int(input('Primeiro número: '))
numero2 = int(input('Segundo número: '))
print('''[1] SOMA\n[2] MULTIPLICAÇÃO\n[3] MAIOR
[4] NOVOS VALORES\n[5] QUIT''')
opcao = int(input('Digite a opção: '))

while opcao not in range(1, 6):
    print('Opção inválida, por favor tente novamente!')
    opcao = int(input('Digite uma opção: '))
while opcao != 5:
    if opcao == 1:
        soma = numero1 + numero2
        print('A soma dos valores inseridos = {}'.format(soma))
    elif opcao == 2:
        multplicacao = numero1 * numero2
        print('{} x {} = {}'.format(numero1, numero2, multplicacao))
    elif opcao == 3:
        if numero1 > numero2:
            print('O maior valor é {}'.format(numero1))
        else:
            print('O maior valor é {}'.format(numero2))
    if opcao == 4:
        print('Insira os novos valores:')
        numero1 = int(input('Primeiro número: '))
        numero2 = int(input('Segundo número: '))
    print('[1] SOMA\n[2] MULTIPLICAÇÃO\n[3] MAIOR\n'
          '[4] NOVOS VALORES\n[5] QUIT')
    opcao = int(input('Digite a opção: '))
    while opcao not in range(1, 6):
        print('Opção inválida, por favor tente novamente.')
        opcao = int(input('Digite uma opção: '))
print('Programa encerrado.')
