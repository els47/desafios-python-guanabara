# Escreva um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²

# Recebendo os valores da largura e altura de uma parede

altura = int(input('Digite o valor da altura:'))
largura = int(input('Digite o valor da largura:'))

# Calculando a área

area = altura * largura

# Calculando a quantidade necessária de tinta em litros

tinta_litros = area / 2
print('A quantidade de tinta em litros é:', tinta_litros)
