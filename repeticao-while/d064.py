# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n = 0
contador = 0
soma = 0
n = int(input('Digite um novo número inteiro. Se quiser parar, digite 999: '))

while n != 999:
    soma += n
    contador +=1
    n = int(input('Digite um novo número inteiro. Se quiser parar, digite 999: '))
print(f'O programa foi finalizado! Você digitou {contador} números e a soma deles é {soma}.')
