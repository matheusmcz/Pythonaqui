quantidade = int(input('Quantos termos você deseja ver? '))
t1 = 0
t2 = 1
contador = 0
print('{} → {} '.format(t1, t2), end='')
while contador < quantidade:
    contador = contador + 1
    t3 = t1 + t2
    print('→ {} '.format(t3), end='')
    t1 = t2
    t2 = t3
print('→ FIM')
