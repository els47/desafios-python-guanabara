# Faça um programa que leia um ano qualquer e mostre se ele é bissexto

# Recebendo um ano qualquer

ano = int(input('Digite um ano qualquer:'))

# Demonstrando se o ano é bissexto ou não

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Este é um ano bissexto!')
else:
    print('Este não é um ano bissexto')
