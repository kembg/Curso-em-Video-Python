import random
# maior = menor = soma = i = 0
# op = 'S'
# while op == 'S':
#     n = int(input('digite um número : '))
#     i += 1
#     soma += n
#     if i == 1:
#         maior = menor = n
#     else:
#         if n > maior:
#             maior = n
#         if n < menor:
#             menor = n
#     op = input('quer continuar [S/N] : ').strip().upper()
# print('''Você digitou {} números
# A média entre eles é {:.2f}
# O maior foi {}
# o menor foi {}'''.format(i, soma/i, maior, menor))


n = random.randint(0,3)
print(n)