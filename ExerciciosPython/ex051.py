p1 = int(input('insira o primeiro termo : '))
r = int(input('insira a razão da pa : '))
decimo = p1 + (10 - 1) * r
for i in range(p1, decimo, r):
    print(i)
