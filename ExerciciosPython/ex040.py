n1 = float(input('Digite a primeira nota : '))
n2 = float(input('Digite a segunda nota : '))
media = (n1+n2)/2

if media >= 7.0:
    print('APROVADO\nMédia = {}'.format(media))
elif 7 > media >= 5:
    print('RECUPERAÇÃO\nMédia = {}'.format(media))
else:
    print('REPROVADO\nMédia = {}'.format(media))