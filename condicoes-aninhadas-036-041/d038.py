# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: O primeiro valor é maior; O segundo valor é maior; Não existe valor maior, os dois são iguais

n1 = int(input('Digite um valor inteiro:'))
n2 = int(input('Digite outro valor inteiro:'))

if n1 > n2:
    print(f'O primeiro valor {n1} é maior.')
elif n1 < n2:
    print(f'O segundo valor {n2} é maior.')
else:
    print('Não existe valor maior, os dois são iguais.')