import math
import random
import pygame

##desafio 016
# num = float(input('digite um numero : '))
# print('o numero {} como inteiro é {}'.format(num, int(num)))

##desafio 017
# co = float(input('valor do cateto oposto : '))
# ca = float(input('valor do cateto adjacente : '))
# h = math.sqrt(ca**2+co**2)
# h = math.hypot(ca,co)
# print('a hipotenusa é : {:.1f}'.format(h))

##desafio 018
# ang = float(input('digite uum angulo : '))
# print('o senoo do angulo : {:.1f}\no consseno do angulo : {:.1f}\na tangente do angulo : {:.1f}'.format(math.sin(ang), math.cos(ang), math.tan(ang)))

##desafio 019
# a1 = 'a'
# a2 = 'b'
# a3 = 'c'
# a4 = 'd'
# alunos = [a1, a2, a3, a4]
# print(random.choice(alunos))

# # desafio 020
# a1 = 'a'
# a2 = 'b'
# a3 = 'c'
# a4 = 'd'
# alunos = [a1, a2, a3, a4]
# random.shuffle(alunos)
# print(alunos)

##desafio 021
pygame.mixer.init()
pygame.init()

pygame.mixer.music.load('my-humps.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(50)
pygame.event.wait()
