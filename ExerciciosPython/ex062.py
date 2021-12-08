n = int(input('o primeiro termo da PA : '))
r = int(input('a razão da PA : '))
i = 0
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while i < total:
        print(n, end=' ')
        n += r
        i += 1
    print('PAUSA')
    mais = int(input('Quantos mais termos você quer mostrar ? '))
