velho = ''
maioridadeh = 0
novas = 0
soma = 0
menorq20 = 0
for i in range(1, 5):
    nome = (input('digite o nome da pessoa {} :'.format(i))).strip()
    idade = int((input('digite a idade da pessoa {} : '.format(i))))
    sexo = input('digite o sexo da pessoa {} (M/F) : '.format(i)).strip().upper()
    soma += idade
    if i == 1 and sexo == 'M':
        velho = nome
        maioridadeh = idade
    else:
        if idade > maioridadeh and sexo == 'M':
            maioridadeh = idade
            velho = nome
    if idade < 20 and sexo == 'F':
        menorq20 += 1
print('''A média de idade do grupo : {:.1f}
O nome do homem mais velho : {}
Quantidade de mulheres com menos de 20 anos : {}'''.format(soma/(i-1), velho, menorq20))
