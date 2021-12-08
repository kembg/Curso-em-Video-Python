frase = str(input('digite uma frase : ')).strip().upper()
palavras = frase.split()
junta = ''.join(palavras)
contrario = ''
for letra in range(len(junta) - 1, -1, -1):
    contrario += junta[letra]
if contrario == junta:
    print('Temos um palindromo')
else:
    print('não temos um palindromo')
print('a frase digitada foi {} e ao contrário é {}'.format(junta, contrario))
