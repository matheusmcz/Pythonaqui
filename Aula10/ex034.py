print('--' * 5, 'BEM-VINDO!!', '--' * 5)

nome = str(input('\nNome do colaborador: ')).strip().lower()
print('--' * 10)
salario = float(input('Salário: R$'))
dezaumento = (salario * 15) / 100
quinzeaumento = (salario * 10) / 100
if salario <= 1250.00:
    print('Com aumento de 15%, novo salário: R${:.2f}'.format(salario + dezaumento))
else:
    print('Com aumento de 10%, o novo salário: R${:.2f}'.format(salario + quinzeaumento))
