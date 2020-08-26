# Promoção
print('-' *5, 'PROMOÇÃO', '-' *5)
prod = float(input('Valor do produto: '))
desc = (prod*5)/100
print('Valor do desconto R$: {:.2f}\nNovo valor R$: {:.2f}'.format(desc, prod - desc))