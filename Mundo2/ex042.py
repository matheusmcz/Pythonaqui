reta1 = float(input('Tamanho da reta 1: '))
reta2 = float(input('Tamanho da reta 2: '))
reta3 = float(input('Tamanho da reta 3: '))
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('As retas formam um triângulo')
    if reta1 == reta2 == reta3:
        print('Tipo: Equilátero.')
    if reta1 == reta2 != reta3 or reta1 == reta3 != reta2 or reta2 == reta3 != reta1:
        print('Tipo: Isósceles.')
    if reta1 != reta2 != reta3:
        print('Tipo: Escaleno.')
else:
    print('As retas não podem formar um triângulo.')

