# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0 # Soma esse valor com o da variável, no caso da expressão abaixo é 'n'
cont = 0 # Faz a contagem de valores, no caso da expressão abaixo é 'n' + 1

for n in range(6):
    n = int(input('Digite um número inteiro:'))
    if n % 2 == 0:
     soma += n
     cont += 1
print(f'A soma dos números pares é {soma}')
print(f'A quantidade de números pares é {cont}')