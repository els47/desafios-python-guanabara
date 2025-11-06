# Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random

# Gerar número inteiro entre 0 e 10
numero = random.randint(0, 10)

# Receber valor do usuário
palpite = int(input('Digite um número inteiro entre 0 e 10: '))

while palpite != numero:
    print('Seu palpite está errado. Tente novamente!')
    palpite = int(input('Digite um número inteiro entre 0 e 10:'))
print(f'Parabéns! Você deu o palpite correto, que era o número {numero}')