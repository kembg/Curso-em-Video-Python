preco = float(input('digite o preço da compra : '))
print('''Escolha uma opção de pagamento : 
[1] a vista em dinheiro/cheque
[2] a vista no cartão
[3]2x no cartão 
[4]3x ou mais no cartão''')
op = int(input('digite sua opção : '))

if op == 1:
    print('O valor total é {}, com desconto pela forma de pagamento será {}'
          .format(preco, preco * 0.90))
elif op == 2:
    print('O Valor total é {}, com desconto pela forma de pagamento será {}'
          .format((preco, preco * 0, 95)))
elif op == 3:
    print('O preço a pagar é {}'.format(preco))
elif op == 4:
    parcela = int(input('Em quantos parcelas ?'))
    print('sua compra parcelada em {:.2f} vezes, terá parcelas de {}, custando no total {}'
          .format(parcela, (preco * 1.20) / parcela, preco * 1.20))
