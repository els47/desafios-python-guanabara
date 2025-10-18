# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu

import random

# Gerar número inteiro entre 0 e 5
numero = random.randint(0, 5)

# Receber valor do usuário
usuario = int(input('Digite um número inteiro entre 0 e 5:'))

# Condição para o usuário descobrir o número (em loop até o usuário acertar)

if usuario == numero:
    print('Você venceu!')
else:
    print(f'Você perdeu, o número aleatório foi o {numero}. Tente novamente!')