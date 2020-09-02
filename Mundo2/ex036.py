nome = str(input('Insira seu nome: ')).strip().lower()
valorcasa = float(input('Insira o valor da casa: R$'))
salariocomprador = float(input('Insira o seu salario: R$'))
tempofinanciamento = int(input('Tempo do financiamento /meses: '))
mensalidade = valorcasa / tempofinanciamento
limitemensalidade = (salariocomprador * 30) / 100
if mensalidade <= limitemensalidade:
    print('Financiamento aprovado!')
    print('Nome do comprador: {}'.format(nome.capitalize()))
    print('Valor do imóvel: R${}'.format(valorcasa))
    print('Tempo do Financiamento: {} meses; Valor da mensalidade: R${}'.format(tempofinanciamento, mensalidade))
else:
    print('Financiamento recusado!')
    print('O valor da mensalidade ultrapassa 30% do seu salário.')
