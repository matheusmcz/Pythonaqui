print('{:=^40}'.format('TABUADA!'))
numero = int(input('NÚMERO: '))
for c in range(1, 11):
   print('[{} x {} = {}]'.format(numero, c, numero*c))
