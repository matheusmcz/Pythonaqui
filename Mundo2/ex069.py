mulher = homem = adulto = 0


while True:
    print('{: ^40}'.format('CADASTRO POSTO B.B 2:'))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade > 18:
        adulto += 1
    if sexo in 'M':
        homem += 1
    if sexo in 'F':
        if idade < 20:
            mulher += 1
    opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'Quantidade + 18 anos: {adulto}')
print(f'Total de homens cadastrados: {homem}')
print(f'Total mulheres menores 20 anos: {mulher}')
