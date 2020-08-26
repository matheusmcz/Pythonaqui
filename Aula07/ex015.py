# Aluguel de carro
print('-' *5, 'ALUGUEL AUTOMOVEL', '-' *5)

dias = int(input('QUantidade de dias alugados: '))
km = float(input('Quantidade de Km rodados:'))
valordia = dias * 60
valorkm = km * 0.15
print('O valor a pagar será de R${:.2f}'.format(valordia + valorkm))
print('----' *8)