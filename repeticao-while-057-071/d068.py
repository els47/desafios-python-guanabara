# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

while True:
    jogador = int(input('Digite um valor: '))
    computador = randint (0, 11)
    total = jogador + computador 
    tipo = ' ' # Cria a variável antes do loop interno e, com isso, pode ser usada nas condições seguintes
    while tipo not in 'PI': # Forçar resposta a ser P ou I e desconsiderar qualquer outra letra
        tipo = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. O total foi {total}.')
    if tipo == 'P' and total %2 == 0:
        print("Parabéns, você venceu!")
        break
    elif tipo == 'I' and total %2 != 0:
        print('Parabéns, você venceu!')
        break
    else:
        print('Não foi dessa vez, tente novamente!')
        break