# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

# Comprimento das retas

c1 = int(input('Digite o comprimento da reta:'))
c2 = int(input('Digite o comprimento da reta:'))
c3 = int(input('Digite o comprimento da reta:'))

# Calculando se é possível formar um triângulo

if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    print('É possível formar um triângulo!')
else:
    print('Não é possível formar um triângulo!')