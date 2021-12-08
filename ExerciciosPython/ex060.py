from math import factorial
n = int(input('digite um número : '))
i = n
print('Calculando fatorial {}!'.format(n))
while i > 0:
    print('{}'.format(i), end='')
    print(' x ' if i > 1 else ' = ', end='')
    i -= 1
print(factorial(n))
