# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.00.
# C) Qual é o nome do produto mais barato.

total = prod_mil = prod_menor = cont = 0
barato = ' '

while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    cont += 1 # Contabiliza quando um produto é cadastrado

    total += preco

    if preco > 1000:
        prod_mil += 1

    if cont == 1: # Avaliação do primeiro produto
        prod_menor = preco # O produto mais barato será referente ao preço desse primeiro produto
        barato = nome
    else:
        if preco < prod_menor:
            prod_menor = preco  
            barato = nome

    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break
print(f'O total gasto na compra foi de R${total}')
print(f'{prod_mil} produtos tiveram valor acima de R$1000.00')
print(f'O produto mais barato foi o {barato}, que custou {prod_menor}')