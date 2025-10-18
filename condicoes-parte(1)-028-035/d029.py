# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7.00 por cada km acima do limite

# Lendo a velocidade de um carro

velocidade = int(input('Digite a velocidade:'))

if velocidade > 80:
    print(f'Você ultrapassou a velocidade permitida e deverá pagar R${(velocidade - 80) * 7} de multa')
else:
    print('Você estava dentro do limite de velocidade!')