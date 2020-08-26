# Conversão de medidas
print('-' *5, 'CONVERSÃO DE MEDIDAS', '-' *5)
m = float(input('Insira a medida em metros: '))
print('{}m equivale a: \n{}Km, {}Hm, \n{}dam, {}dcm, \n{}cm, {}mm.'.format(m, m/1000, m/100, m/10, m*10, m*100, m*1000))