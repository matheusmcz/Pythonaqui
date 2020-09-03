print('{:-^40}'.format(' FUNERARIA AGRÁRIA '))
valorproduto = float(input('TOTAL: R$'))
print('''FORMA DE PAGAMENTO:
[ 1 ] À VISTA: 
[ 2 ] 1x CARTÃO:
[ 3 ] 2x CARTÃO:
[ 4 ] 3X OU MAIS:''')
pagamento = int(input('FORMA DE PAGAMENTO: '))
if pagamento == 1:
    print('\nÀ VISTA COM 10% DESCONTO: R${:.2f}'.format(valorproduto - (valorproduto * 10) / 100))
elif pagamento == 2:
    print('\n1x NO CARTÃO, 5% DESCONTO: R${:.2f}'.format(valorproduto - (valorproduto * 5) / 100))
elif pagamento == 3:
    print('\n2x CARTÃO: R${:.2f}'.format(valorproduto))
    print('\nQUANTIDADE DE PARCELAS - 2x R${:.2f}'.format(valorproduto / 2))
elif pagamento == 4:
    print('{:-^40}'.format(' QUANTIDADE DE PARCELAS '))
    parcelas = int(input('- '))
    juros = valorproduto + ((valorproduto * 20) / 100)
    print('VALOR COM JUROS 20%: R${:.2F}'.format(juros))
    print('{}x CARTÃO: {}'.format(parcelas, juros / parcelas))
