# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número inteiro:'))
contador = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ')
        contador += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {n} foi divisível {contador} vezes.')
if contador == 2:
    print('E por isso ele é um número primo!')
else:
    print('E por isso ele não é um número primo!')