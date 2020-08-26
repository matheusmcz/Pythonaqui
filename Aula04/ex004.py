a = input('Insira algo: ')
print('O tipo primito é: {}, Somente espaço? {}, É numérico? {}'.format(type(a), a.isspace(), a.isnumeric()))
print('É alfanumerico? ', a.isalnum())
