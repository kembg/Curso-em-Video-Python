from random import choice

print('''Selecione uma opção para joar com o computador!
[1]pedra
[2]papel
[3]tesoura''')
op = int(input('sua opção : '))
if op > 3:
    print('jogada invalida')
jogadas = ['pedra', 'papel', 'tesoura']
oppc = choice(jogadas)
if oppc == jogadas[op - 1]:
    print('Você empatou!!!\nO computador também jogou {}'.format(oppc))
elif oppc == 'pedra' and jogadas[op - 1] == 'tesoura' or oppc == 'papel' and jogadas[
    op - 1] == 'pedra' or oppc == 'tesoura' and jogadas[op - 1] == 'papel':
    print('Você perdeu :(\nO computador jogou {}'.format(oppc))
else:
    print('Você ganhou!!!\nO computador jogou {}'.format((oppc)))
