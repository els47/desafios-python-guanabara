# Refaça o DESAFIO 051 (Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão), lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro_termo = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
termo = primeiro_termo
cont = 1

while cont <=10:
    print(f"{termo} - ", end='')
    termo += razao
    cont += 1
print("Fim")