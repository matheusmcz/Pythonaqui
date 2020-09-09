produtocaro = ''
produtobarato = ''
soma = contador1000 = contador = valorbarato = 0
while True:
    produto = str(input('Nome do produto: ')).strip().title()
    valor = float(input('Valor R$: '))
    soma += valor
    contador += 1
    if valor >= 1000:
        produtocaro = produto
        contador1000 += 1
    if contador == 1:
        produtobarato = produto
        valorbarato = valor
    else:
        if valor < valorbarato:
            produtobarato = produto
            valorbarato = valor
    opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'TOTAL: R${soma:.2f}')
print(f'{contador1000} produto(s) acima de R$1000: {produtocaro}')
print(f'{produtobarato} foi o mais barato, custando R${valorbarato:.2f}')
