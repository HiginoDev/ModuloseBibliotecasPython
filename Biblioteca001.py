#import math
#num = int(input('Digite um número qualquer para saber sua raiz quadrada:'))
#raiz = math.sqrt(num)
#print('A raiz quadrada de {} é igual a {} '.format(num, math.ceil(raiz)))

#import math
#num = float(input('Digite um número qualquer:'))
#print('O número digitado foi {} e sua porção inteira é {}'.format(num, math.trunc(num)))

#Calcular ãngulo, seno, cosseno e tangente
#import math
#ângulo = float(input( 'Digite um numero de um ângulo: '))
#seno = math.sin(math.radians(ângulo))
#cosseno = math.cos(math.radians(ângulo))
#tangente = math.tan(math.radians(ângulo))
#print('Para um ângulo de {} teremos um seno de: {:.2f} e um consseno de {:.2f} e sua tangente de {:.2f}'.format(ângulo, seno, cosseno, tangente))

# O sistema escohe com a biblioteca RANDOM o aluno que vai ser sorteado
#import random
#n1 = input('Digite o nome do primeiro aluno: ')
#n2 = input('Digite o nome do segundo aluno: ')
#n3 = input('Digite o nome do terceiro aluno: ')
#n4 = input('Digite o nome do quarto aluno: ')
#lista = [n1,n2,n3,n4]
#escolhido = random.choice(lista)
#print('O aluno sorteado foi {}'.format(escolhido))

#Embaralha os nomes da lista com o modulo random (shuffle)
#from random import shuffle
#n1 = input('Informe o primeiro aluno: ')
#n2 = input('Informe o segundo aluno: ')
#n3 = input('Informe o terceiro aluno: ')
#n4 = input('Informe o quarto aluno: ')
#lista = [n1,n2,n3,n4]
#shuffle(lista)
#print('A ordem de apresentação será: ')
#print(lista)

from pygame import mixer
mixer.init()
mixer.music.load('bad-liar.mp3')
mixer.music.play()
x = input('Digite algo para parar a musica...')

