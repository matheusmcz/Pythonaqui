numero = int(input('Digite um número: '))
continuacao = str(input('Deseja continuar? [S/N]: ')).strip().upper()
contador = 1
media = numero / contador
soma = numero
maior = numero
menor = numero
while continuacao not in 'N':
    contador = contador + 1
    numero = int(input('Digite um número: '))
    continuacao = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    soma = soma + numero
    media = soma / contador
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
print('{} números digitados. Média de {}'.format(contador, media))
print('{} foi o maior valor, {} foi o menor.'.format(maior, menor))
