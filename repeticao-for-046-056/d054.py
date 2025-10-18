# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
atual = date.today().year

cont_maior = 0
cont_menor = 0

for i in range(7):
    nasc = int(input('Digite seu ano de nascimento:  '))
    idade = atual - nasc
    if idade >= 18:
        cont_maior += 1
    else:
        cont_menor += 1
print(f'Ao todo tivemos {cont_maior} pessoas maior(es) de idade e {cont_menor} pessoas menor(es) de idade.')

