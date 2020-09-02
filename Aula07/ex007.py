# Media (nt1 + nt2)/2 pode ser assim tambem
print('-' * 5, 'MEDIA', '-' * 5)
name = str(input('Insira o nome do aluno: ')).strip().split()
nota1 = float(input('Nota oficial 1: '))
nota2 = float(input('Nota oficial 2: '))
media = (nota1 + nota2) / 2
print('A média do aluno {} foi = {:.2f}'.format(name[0].capitalize(), media))
if media >= 6.0:
    print('Parabéns aluno aprovado! ')
else:
    print('Tais lascado {}!'.format(name[0].capitalize()))
