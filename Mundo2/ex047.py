import time
print('{:=^40}'.format('CONTAGEM REGRESSIVA'))
for c in range(50, 0, -2):
    time.sleep(1)
    print(c)
print('FIM')