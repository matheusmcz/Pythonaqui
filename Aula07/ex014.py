# Converção temperatura
print('-' *5, 'CONVERSÃO DE TEMP.', '-' *5)
tempc = float(input('Informe temp. °C: '))
tempf = ((9*tempc)/5)+32
print('{0}°C equivale a {1}°F.'.format(tempc, tempf))
