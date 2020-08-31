print('-' *5, '???', '-' *5)

frase = str(input('Digite uma frase: ')).strip().lower()

print('A letra (a) aparece {} vezes'.format(frase.count('a')))
print('A primeira letra (a) aparace na posição {}'.format(frase.find('a')+1))
print('A ultima letra (a) aparece na posição {}'.format(frase.rfind('a')))
