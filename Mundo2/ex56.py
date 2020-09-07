media = 0
nomehomemmaisvelho = 0
idadehomemmaisvelho = 0
mulheresmenor20 = 0
for c in range(1, 5):
    print('--' * 5, '{} PESSOAS'.format(c), '--' * 5)
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    media = media + idade / 4
    if c == 1 and sexo in 'Mm':
        nomehomemmaisvelho = nome
        idadehomemmaisvelho = idade
    if sexo in 'Mm' and idade > idadehomemmaisvelho:
        nomehomemmaisvelho = nome
        idadehomemmaisvelho = idade
    if sexo in 'Ff' and idade < 20:
        mulheresmenor20 = mulheresmenor20 + 1
print('--' * 5, 'ANALISE', '--' * 5)
print('\nMédia de idade do grupo: {} anos;'.format(media))
print('{} é o homem mais velho, com {} anos;'.format(nomehomemmaisvelho, idadehomemmaisvelho))
print('Existem {} mulheres abaixo dos 20 anos.'.format(mulheresmenor20))
