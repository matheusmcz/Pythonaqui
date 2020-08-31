print('-' *5, 'Primeiro e último nome de uma pessoa', '-' *5)

nomecompleto = str(input('Nome completo: ')).strip()
nomejunto = nomecompleto.split()
print('Seu primeiro nome é: {}'.format(nomejunto[0]))
print('Seu ultimo nome é: {}'.format(nomejunto[-1]))
