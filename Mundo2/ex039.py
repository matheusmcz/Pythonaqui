import datetime

idade = int(input('Informe seu ano de nascimento: '))
periodoalismento = datetime.date.today().year - idade
if periodoalismento < 18:
    print('Você ainda vai se alistar!')
    print('Faltam {} anos.'.format(18 - periodoalismento))
elif periodoalismento == 18:
    print('Está na hora de se alistar!')
elif periodoalismento > 18:
    print('Você já passou {} anos do prazo.'.format(periodoalismento - 18))
