# Escreva um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

# Recebendo um valor
valor = int(input('Digite um número inteiro:'))

# Imprimindo a tabela
for i in range(1, 11):
    print(f'{valor *i}', end = " ")

