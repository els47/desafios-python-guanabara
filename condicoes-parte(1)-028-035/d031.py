# Desenvolva um programa que pergunta a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0.50 por km para viagens de até 200km a R$0.45 para viagens mais longas

# Recebendo a distância da viagem em km

distancia = int(input('Digite a distância da viagem:'))

# Calculando o preço da passagem

if distancia <= 200:
    print(f'O preço da passagem é: {distancia * 0.50}')
else:
    print(f'O preço da passagem é: {distancia * 0.45}')