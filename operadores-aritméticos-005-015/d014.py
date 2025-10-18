# Escreva um programa que converta uma temperatura digitada em ºC e connverta para ºF. Considere que 1ºC representa 33ºF.

# Recebendo a temperatura
c = float(input('Digite a temperatura:'))

# Calculando a conversão
print(f'A temperatura na escala Farenheit é {((9 * c)/5) + 32}')

