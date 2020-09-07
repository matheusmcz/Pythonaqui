sexo = str(input('Informe o Sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    print('Informação inválida, você deve digitar: \n'
          'M para Masculino\n'
          'F para femenino.')
    sexo = str(input('Informe o Sexo [M/F]: ')).strip().upper()[0]
print('FIM')
