nome = 'kennedy'
# para dar espaço :
print('prazer em te conhecer {:20}!'.format(nome))
# para dar espaço para direita
print('prazer em te conhecer {:>20}!'.format(nome))
# para dar espaço a esquerda
print('prazer em te conhecer {:<20}!'.format(nome))
# para centralizar entre os espaços
print('prazer em te conhecer {:^20}!'.format(nome))
# para centralizar com algum caractere
print('prazer em te conhecer {:@^20}!'.format(nome))

# estudando formatação de numeros
# n1 = int(input('digite um num : '))
# n2 = int(input('dgitie outro : '))
# s = n1 + n2
# sub = n1 - n2
# d = n1 / n2
# m = n1 * n2
# di = n1 // n2
# e = n1**n2
# print('a soma é {}, a subtração é {}, a divisão é {:.2f}'.format(s, sub, d))
# print('a divisão inteira é {}, a exponenciação é {} '.format(di, e))

##desafio 005
# num = int(input("digite um num : "))
# print('numero : {} \nsucessor : {}\nantecessor : {}'.format(num, num+1, num-1))

##desafio 006
# num = int(input('digite um num : '))
# print('numero : {}\ndobro : {}\ntriplo : {}\nraiz quadrada : {}'.format(num, num*2, num*3, num**0.5))

# ##desafio 007
# n1 = int(input('digite a primeira nota : '))
# n2 = int(input('digite a segunda nota : '))
# print('a média é : ', (n1+n2)/2)

##desafio 008
# metros = float(input('digite o valor em metros para a conversão : '))
# print('em centimetros {}\nem milimetros : {}'.format(metros*100, metros*1000))

# ##desafio 009
# num = int(input('digite um numero : '))
# print('{}x1={}\n{}x2={}\n{}x3={}\n{}x4={}\n{}x5={}\n{}x6={}\n{}x7={}\n{}x8={}\n{}x9={}\n{}x10={}\n'
#       .format(num, num*1, num, num*2, num, num*3, num, num*4, num, num*5, num, num*6, num, num*7, num, num*8, num, num*9, num, num*10))

##desafio 010
# dinheiro = int(input('quanto dinheiro você tem ? '))
# print('você pode comprar {:.2f} dolares'. format(dinheiro*3.27))

##desafio 011
# altura = float(input('qual a altura da parede ? '))
# largura = float(input('qual a largura da parede ? '))
# area = altura*largura
# print('vão ser necessários {:.1f} litros de tinta'.format(area/2))

##desafio 012
# preco = float(input('digite o preço : '))
# print('preço com desconto é ', preco*0.95)

##desafio 13
salario = float(input('digite o salário : '))
print('o salário com aumento de 15% é :', salario*1.15)