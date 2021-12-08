from datetime import date

nasc = int(input('digite seu ano de nascimento : '))
idade = date.today().year - nasc

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFATIL')
elif idade <= 19:
    print('JÚNIOR')
elif idade <= 24:
    print('SÊNIOR')
else:
    print('MASTER')