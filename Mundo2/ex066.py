contador = soma = numero = 0
while True:
    numero = int(input('Valor, [777 para finalizar]: '))
    if numero == 777:
        break
    soma += numero
    contador += 1
print(f'Você informou {contador} valores, que somados = {soma}.')
