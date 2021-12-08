from datetime import date

maior = 0
menor = 0

for i in range(1, 8):
    ano = int(input('digite o ano de nascimento da pessoa {} :'))
    idade = date.today().year - ano
    if idade < 18:
        menor += 1
    else:
        maior += 1
print('Entre as 7 pessoas :\n {} são maiores de idade\n{} são menores de idade'.format(maior, menor))
