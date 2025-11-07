# Refaça o DESAFIO 051 (Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão), lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.


# Recebendo o primeiro termo e a razão

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão PA: '))
c = 1
decimo_termo = primeiro_termo + (10 - 1) * razao

while c <= 10: # Deve acontecer 9 iterações para mostrar os 10 primeiros termos da progressão
    for c in range(primeiro_termo, decimo_termo, razao):
        print(c, end= ' ')
    c += 1 # Controla a quantidade de iterações que será feito o laço for
