media = 0
homemmaisvelho = 0
nomehomem = 0
mulhermaisnova = 0
quantidademulheres = 0
for c in range(1, 5):
    print('--' * 5, '{}ª PESSOA'.format(c), '--' * 5)
    pessoa = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = (input('Sexo [M/F]: ')).strip().upper()
    media = media + idade / 4
    if c == 1 and sexo in 'Mm':
        homemmaisvelho = idade
        nomehomem = pessoa
    if sexo in 'Mm' and idade > homemmaisvelho:
        homemmaisvelho = idade
        nomehomem = pessoa
    if sexo in 'Ff' and idade < 20:
        quantidademulheres = quantidademulheres + 1
print('\nA média de idade é de {} anos.'.format(media))
print('{} é o homem mais velho, com {} anos.'.format(nomehomem, homemmaisvelho))
print('Quantidade de mulheres abaixo dos 20 anos: {}'.format(quantidademulheres))
