from math import pow
nome = str(input('Insira seu nome: ')).strip().lower()
altura = float(input('Altura: '))
peso = float(input('Peso:'))
imc = peso / pow(altura, 2)
print('Paciente: {}'.format(nome.title()))
if imc <= 18.5:
    print('Abaixo do Peso.')
elif 18.5 < imc <= 25:
    print('Peso Ideal.')
elif 25 < imc <= 30:
    print('Sobrepeso.')
elif 30 < imc <= 40:
    print('Obesidade.')
elif imc > 40:
    print('Obesidade Mórbida.')
