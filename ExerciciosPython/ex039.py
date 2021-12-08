sexo = input('digite seu sexo : (M/F)').upper().strip()
nasc = int(input('digite seu ano de nascimento : '))
idade = 2021-nasc

if sexo != 'F':
    if idade > 18:
        print('você deveria se alistar há {} anos'.format(idade-18))
    elif idade == 18:
        print('você deve se alistar nesse ano')
    else:
        print('você deve se alistar em {} anos'.format(18-idade))
else:
    print('voce não tem obrigação de se alistar')