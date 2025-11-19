# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# a) Quantas vezes apareceu o valor 9
# b) Em que posição foi digitado o primeiro valor 3
# c) Quais foram os números pares

n = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')), int(input('Digite outro valor: ')), int(input('Digite outro valor: ')))

print(f'Os valores digitados foram: {n}')

if 9 in n:
    print(f'O valor 9 apareceu {n.count(9)} vezes')
else:
    print('O valor 9 não foi digitado')

if 3 in n:
    print(f'O primeiro valor 3 digitado está na {n.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado')

print('Os valores pares foram: ', end='')
for par in n:
    if par %2 == 0:
        print(par, end=" ")