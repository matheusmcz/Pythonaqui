from datetime import date
maiordeidade = 0
menordeidade = 0
for c in range(1, 8):
    anonascimento = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = date.today().year - anonascimento
    if idade < 18:
        menordeidade = menordeidade + 1
    elif idade >= 18:
        maiordeidade = maiordeidade + 1

print('Você informou {} pessoas menores de idade.'.format(menordeidade))
print('Você informou {} pessoas maiores de idade.'.format(maiordeidade))
