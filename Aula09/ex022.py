print('-' *5, 'NOME MAIUSCULO/MENUSCULO', '-' *5)

# .strip para elimitar os espaços antes e depois da str

nome = str(input('Insira seu nome completo: ')).strip()
nomeseparado = nome.split()
nomejunto = ''.join(nomeseparado)
print('Nome todo Maiusculo: {}' .format(nome.upper()))
print('Nome todo Minusculo: {}' .format(nome.lower()))
print('Total de letras: {}' .format(len(nomejunto)))
print('Total de letras no primeiro nome: {}' .format(len(nomeseparado[0])))
