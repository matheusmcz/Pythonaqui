numero = 0
contador = 0
soma = 0
nome = 'Gustavo'
idade = 30
salario = 10532.66
while True:
    numero = int(input('Digite um valor: '))
    if numero == 777:
        break
    soma += numero
    contador += 1

print(f'{nome} tem {idade}, informou {contador} números, somados = {soma} e ganha R${salario}')
