# Escreva um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere: US$1.00 = R$3.27

# Recebendo o valor na carteira

real = float(input('Digite o valor na sua carteira:R$'))

# Calculando a quantidade de dólares

dolar = float(real / 3.27)
print('A quantidade de dólares que você pode comprar é:', dolar)