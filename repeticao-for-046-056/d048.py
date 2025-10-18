# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

# Calculando os números

soma = 0
cont = 0
for c in range (1, 501):
    if c % 2 != 0 and c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print('A soma de todos os valores solicitados é:', soma)
print('E a quantidade de números solicitados é:', cont)
        


# Outra forma: 
# for c in range (1, 501, 2):
#     if c % 3 == 0:
#         print(c, end = ' ')

# soma é um acumulador de valores
# contador geralmente soma 1 a cada repetição
