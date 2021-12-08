# ##desafio 022
# num = int(input('digite um numero : '))
# print('unidade : ', num // 1 % 10)
# print('dezena : ', num // 10 % 10)
# print('centena : ', num // 100 % 10)
# print('milhar : ', num // 1000 % 10)

##desafio 023
# c = str(input('Em que cidade voce nasceu ? ')).strip().lower()
# print(c[:5] == 'santo')

##desafio 024
# nome = str(input('digite seu nome : ')).lower()
# print('silva' in nome)

##desafio 025
# frase = str(input('digite uma frase : ')).strip().upper()
# print('A frase tem {} letras A'.format(frase.count('A')))
# print('A letra A aparece pela primira vez na posição {} '. format(frase.find('A')+1))
# print('A letra A aparece pela ultima vez na posicao {}'.format(frase.rfind('A')+1))

##desafio 026
n = str(input('digite seu nome completo : ')).strip()
nome = n.split()
print('seu primeiro nome é {}\nseu último nome é {}'.format(nome[0], nome[len(nome)-1]))
