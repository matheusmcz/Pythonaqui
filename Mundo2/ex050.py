soma = 0
contador = 0
for c in range(1, 7):
    num = int(input('Número: '))
    if num % 2 == 0:
        soma = soma + num
        contador = contador + 1
print('{} números pares no range... Somados = {}'.format(contador, soma))
