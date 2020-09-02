#if elif else

nome = str(input('Digite seu nome: ')).strip().lower()
if nome == 'matheus':
    print('Seu nome é lindo {}!'.format(nome.capitalize()))
elif nome == 'joão' or nome == 'maria' or nome == 'josé':
    print('Seu nome é bastante popular {}"'.format(nome.capitalize()))
else:
   print('Seu nome é bem normalzinho! {}'.format(nome.capitalize()))
print('Tenha um bom dia.')
