
frase = str(input('DIGITE UMA FRASE: ')).strip().upper()
fraseseparado = frase.split()
frasejunto = ''.join(fraseseparado)
inverso = frasejunto[::-1]
print('{} = {}'.format(frasejunto, inverso))
if frasejunto == inverso:
    print('TEMOS UM PALÍNDROMO!')
else:
    print('NÃO É UM PALÍNDROMO.')
