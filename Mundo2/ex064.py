soma = 0
contador = 0
while contador != 777:
    contador = contador + 1
    numero = int(input('Digite qualquer número [777 stop]: '))
    soma = soma + numero
    if numero == 777:
        print('A soma de todos os {} números informados foi = {}'.format(contador - 1, soma-777))
        contador = 777
print('')
