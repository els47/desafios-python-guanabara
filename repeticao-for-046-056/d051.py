# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão PA: '))
decimo_termo = primeiro_termo + (10 - 1) * razao # fórmula do décimo termo de uma PA (temro que você quer - 1)

for c in range(primeiro_termo, decimo_termo, razao):
    print(c, end= ' ')
