from random import randint
opcoes = ('pedra', 'papel', 'tesoura')
maquina = randint(0, 2)
print('{:-^40}'.format(' PEDRA, PAPEL, TESOURA!!! '))

print('''ESCOLHA:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
print('==' * 10)
jogador = int(input('QUAL SUA ESCOLHA? '))

print('==' * 10)
if maquina == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VOCÊ VENCEU!')
    elif jogador == 2:
        print('MAQUINA VENCEU!')
    else:
        print('JOGADA INVÁLIDA')
elif maquina == 1:
    if jogador == 0:
        print('MAQUINA VENCEU!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VOCÊ VENCEU!')
    else:
        print('JOGADA INVÁLIDA')
elif maquina == 2:
    if jogador == 0:
        print('VOCÊ VENCEU!')
    elif jogador == 1:
        print('MAQUINA VENCEU!')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
