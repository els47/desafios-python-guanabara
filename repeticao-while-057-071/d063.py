# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci (A Sequência de Fibonacci é uma série numérica onde cada termo é a soma dos dois anteriores, começando com \(0\) e \(1\)Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8)

# Recebendo um número inteiro 
n = int(input("Digite o número de termos que quer mostrar: "))
termo_1 = 0
termo_2 = 1
print(f'{termo_1} - {termo_2}', end='')
cont = 3

while cont <= n:
    termo_3 = termo_1 + termo_2
    print(f' - {termo_3}', end='')
    termo_1 = termo_2
    termo_2 = termo_3
    cont += 1
print(" - Fim")