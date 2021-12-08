num = int(input('digite um numero inteiro : '))
op = int(input('''Digite uma opção para converter seu número : 
[1] para binário
[2] para octal
[3] para hexadecimal 
'''))

if op == 1:
    print('o numero {} convertido para binario é {}'.format(num, bin(num)))
elif op == 2:
    print('o numero {} convertido para octal é {}'.format(num, oct(num)))
elif op == 3:
    print('o numero {} convertido para hexidecimal é {}'.format(num, hex(num)))
else:
    print('essa não é umma opção válida')