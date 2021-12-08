#--tipos primitivos
# n1 = int(input('digite o primeiro num: '))
# n2 = int(input('digite o segundo num: '))
# #print('a soma entre', n1,'e',n2,'vale', n1+n2)
# print('a soma entre {} e {} vale {}'.format(n1, n2, n1+n2))

variavel = input('digite um tipo primitivo: ')
print('A variavel é int = {}, float = {}, string = {}, boolean = {}'.format(variavel.isalnum(), variavel.isdecimal(), variavel.isalpha(), variavel.isidentifier()))
