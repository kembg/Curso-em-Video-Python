from random import randint

i = 0
nc = randint(0, 10)
print(nc)
nu = int(input('''Sou seu computador e pensei em um número.
Tente advinhar : '''))
while nu != nc:
    if nc > nu:
        print('Quase! Tente um valor mais alto')
    else:
        print('Poxa! Tente um valor mais baixo')
    nu = int(input('Errou! Tente novamente com outro número : '))
    i += 1
print('''Você acertou! O número escolhido pelo computador era : {}
Foram necessários {} tentativas '''.format(nc, i))
