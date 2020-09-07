#enquanto não pegar:
    #passo
#pega
'''ou seja'''
'''while not apple:
    passo
pega'''
'''c = 1
while c != 0:
    c = int(input('Digite um número: '))
print('Fim')'''

impar = 0
par = 0
n = 1
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
           par = par + 1
        else:
            impar = impar + 1
print('Você inseriu {} números PARES, e {} IMPARES.'.format(par, impar))
