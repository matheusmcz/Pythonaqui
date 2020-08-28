print('-' *5, 'ORDEM DE APRESENTAÇÃO', '-' *5)
from random import sample
aluno1 = input('Aluno 1: ')
aluno2 = input ('Aluno 2: ')
aluno3 = input('Aluno 3: ')
aluno4 = input('Aluno 4: ')
lista = (aluno1, aluno2, aluno3, aluno4)
ordemDeAlunos = sample(lista, k=4)
print('O sorteado foi: {}'.format(ordemDeAlunos))
