import datetime

idade = int(input('Insira o ano de nascimento do atleta: '))
categoria = datetime.date.today().year - idade
if categoria <= 9:
    print('Atleta categoria: MIRIM.')
elif 9 < categoria <= 14:
    print('Atleta categoria: INFANTIL.')
elif 14 < categoria <= 19:
    print('Atleta categoria: JUNIOR.')
elif 19 < categoria <= 20:
    print('Atleta categoria: SÊNIOR.')
else:
    print('Atleta categoria: MASTER.')
