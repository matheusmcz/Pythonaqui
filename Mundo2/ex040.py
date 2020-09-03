nota1 = float(input('Nota Oficial 1: '))
nota2 = float(input('Nota Oficial 2: '))
media = (nota1 + nota2) / 2
if media <= 5:
    print('REPROVADO. \nMEDIA: {:.2f}'.format(media))
elif 5 < media <= 6.9:
    print('RECUPERAÇÃO. \n MEDIA: {:.2f}'.format(media))
else:
    print('APROVADO. \nMEDIA: {:.2f}'.format(media))
