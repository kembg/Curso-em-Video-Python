for i in range(1, 7):
    peso = float(input('digite o peso da pessoa {} : '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('o menor peso foi {}\nO maior peso foi {}'.format(menor, maior))
