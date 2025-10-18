# Faça um programa que leia três números e mostre qual é o maior e qual é o menor

# Recebendo três valores

valor1 = int(input('Digite um valor inteiro:'))
valor2 = int(input('Digite um valor inteiro:'))
valor3 = int(input('Digite um valor inteiro:'))

# Definindo qual é o maior e qual é o menor

if valor2 < valor1 > valor3:
    print(f'{valor1} é o maior valor')
elif valor1 < valor2 > valor3:
    print(f'{valor2} é o maior valor')
else:
    print(f'{valor3} é o maior valor')
if valor2 > valor1 < valor3:
    print(f'{valor3} é o mmenor valor')
elif valor1 > valor2 < valor3:
    print(f'{valor2} é o menor valor')
else:
    print(f'{valor3} é o menor valor')
    

