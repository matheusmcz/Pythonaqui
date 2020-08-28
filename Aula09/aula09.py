# Fatiamento str
# [] serve para lista.
# [9:13] seleciona uma fatia da str. começando no 9 terminando no 13, sem mostrar o ultimo.
# [9:21:2] saltando de 2 em 2.
# [:5] começa do '0' até o 5, eliminando o ultimo.
# [5:] começa do '5' vai até o final.
# [5::3] começa do '5', vai até o final pulando de 3 em 3.
# Analise
# função len(frase), len = comprimento.
# frase.count('o,0,13') o comando vai contar quantas letras 'o' existem na frase, entre caracter 0 e 13.
# frase.find ('deo')
#Transformação
# frase.replace ('Python, Android)
# frase.upper() / frase.lower()
# frase.strip() remove os espaço inuteis, no inicio e no final da str, frase.rstrip elimina pela direita
# frase.lstrip() remove os espaços pela esquerda
# frase.title() captaliza a primeira letra de cada palavra
# frase.split() utiliza os espaço para separar
# '-'.join(frase) para juntas, utilizando o separado das ' '



frase = str(input('Frase: '))
print(len(frase), frase[:15:3], '\n', frase[:10] )