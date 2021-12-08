# Faça um programa que leia um número
# inteiro e diga se ele é ou não um número primo.
p = 0
n = int(input('digite um número : '))
print('o numero {} é divisivel (verde) e não divisivel (vermelho) pelos números : ')
for i in range(1, n + 1):
    if n % i == 0:
        print('\033[32m', end='')
        p += 1
    else:
        print('\33[31m', end='')
    print(i, end=' ')
if p != 2:
    print('''\no número {} foi divisivel por {} números diferentes
Ele não é primo'''.format(n, p))
else:
    print('''\no número {} foi divisivel somente por 1 e ele mesmo
É um número primo'''.format(n))
