# Salario
print('-' *5, 'SALARIO', '-' *5)
sal = float(input('Insira seu salário: R$'))
nvsal = (sal*15)/100
print('Novo salário com 15% de aumento R${:.2f}'.format(sal+nvsal))