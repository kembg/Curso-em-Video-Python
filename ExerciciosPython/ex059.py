from time import sleep

n1 = int(input('digite um número : '))
n2 = int(input('digite um número : '))
op = 0
while op != 5:
    print('''Escolha uma opção: 
[1] Somar os dois números
[2] Multiplicar os dois números
[3] Checar o maior
[4] Digitar novos números
[5] Sair do programa''')
    op = int(input('Sua opção : '))
    if op == 1:
        print('{} + {} = {}'.format(n1, n2, n1+n2))
    elif op == 2:
        print('{} x {} = {}'.format(n1, n2, n1*n2))
    elif op == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        else:
            print('{} é maior que {}'.format(n2, n1))
    elif op == 4:
        n1 = int(input('digite um número : '))
        n2 = int(input('digite um número : '))
    elif op == 5:
        print('Encerrando o programa...')
    else:
        print('opção inválida')
    sleep(2)
