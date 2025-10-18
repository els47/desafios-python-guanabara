# Refaça esse desafio: "# Escreva um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada" só que agora utilizando um laço for.

valor = int(input('Digite um número inteiro:'))

for c in range(1, 11):
    print (f'{valor * c}', end = ' ')