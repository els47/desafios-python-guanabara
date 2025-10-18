# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60.00 por dia e R$0.15 por km rodado

# Recebendo os valores

km_rodados = float(input('Digite a quantidade de km percorridos: '))
dia_alugado = float(input('Digite a quantidade de dias com o carro alugado: '))

# Calculando o preço a pagar pelo aluguel
custo_km = km_rodados * 0.15
custo_dia = dia_alugado * 60.00

# Calculando o custo total
custo_total = custo_km + custo_dia
print(f'O custo do aluguel por dia é {custo_dia} e por km rodado é {custo_km}. O custo total então é {custo_km + custo_dia}')