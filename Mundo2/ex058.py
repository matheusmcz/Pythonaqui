import random
import time
tentativas = 0
print('{:=^40}'.format(' ADIVINHAÇÃO 2.0 '))
time.sleep(1)
print('{: ^40}'.format('Olá, eu sou seu computador...'))
time.sleep(1)
print('{: ^40}'.format('Vamos brincar de advinhação!!!'))
time.sleep(1)
print('{: ^40}'.format('Pensarei em um número entre 1 e 5'))
time.sleep(1)
print('{: ^40}'.format('Tente adivinhar, okay?'))

sorteio = random.randint(1, 5)
escolha = int(input('Qual foi o número? '))

while escolha not in range(1, 6):
    print('Número inválido, você deve escolher entre 1 e 5.'.upper())
    escolha = int(input('Qual foi o número? '))
while escolha != sorteio:
    tentativas = tentativas + 1
    while escolha not in range(1, 6):
        print('Número inválido, você deve escolher entre 1 e 5.'.upper())
        escolha = int(input('Qual foi o número? '))
    if escolha < sorteio:
        print('Errou! Foi maior!!')
        escolha = int(input('Qual número? '))
    if escolha > sorteio:
        print('Errou! Foi menor!')
        escolha = int(input('Qual número? '))
print('Acertou! Você errou {} vezes'.format(tentativas))
