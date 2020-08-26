# Odem de precedencia
# 1 ()
# 2 ** potencia
# 3 * multiplicação, / divisão, // divisão inteira e % resto da divisão
# 4 adição + e subtração -
print('='*10, 'Aritmetica', '='*10)
n1 = int(input('Insira um Valor: '))
n2 = int(input('Insira outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 / n2
p = n1 ** n2
print('O valor da soma é: {}, \nO valor da multiplicação é: {}'.format(s, m))
print('A divisão é igual a: {:.2f}, \nDivisão inteira: {:.2f}'.format(d, di))
print('{} elevado a {} é igual a: {}'.format(n1, n2, p))
