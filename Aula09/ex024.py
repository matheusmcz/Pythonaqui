print('-' *5, 'TEM SANTO?', '-' *5)

cidade = str(input('Insira o nome da Cidade: ')).strip().lower()
print('A cidade informada começa com a palavra Santo? {}'.format(cidade.startswith('santo')))
