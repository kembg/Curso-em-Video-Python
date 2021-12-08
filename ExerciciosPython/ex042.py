l1 = int(input('digite o valor do segmento : '))
l2 = int(input('digite o valor do segmento : '))
l3 = int(input('digite o valor do segmento : '))

if l1 + l2 > l3 or l1 + l3 > l2 or l2 + l3 > l1:
    if l1 == l2 == l3:
        print('forma um triângulo equilátero')
    elif l1 != l2 != l3 != l1:
        print('forma um triângulo escaleno')
    else:
        print('forma um triângulo isosceles')
else:
    print('não forma um triangulo')
