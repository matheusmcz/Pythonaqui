from random import randint
print('{:-^40}'.format('PAR OU IMPAR'))
contadorvitoria = 0
while True:
    numero = int(input('Seu número: '))
    escolha = str(input('PAR OU IMPAR [P/I]: ')).strip().upper()
    pc = randint(0, 10)
    total = numero + pc
    print(f'Sua escolha: {numero}, MAquina {pc}. Total: {total}')
    if escolha in 'P':
        if total % 2 == 0:
            print('VOCÊ GANHOU.')
        else:
            break
    if escolha in 'I':
        if total % 2 != 0:
            print('VOCÊ GANHOU.')
        else:
            break
    contadorvitoria += 1
print(f'FIM DE JOGO. QUANTIDADE DE VITÓRIAS: {contadorvitoria}')
