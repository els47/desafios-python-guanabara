# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

valor_casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o valor do seu salário: R$'))
anos = int(input('Digite em quantos anos você pretende pagar a casa:'))

prestacao_mensal = valor_casa / (anos * 12) # Quantidade de anos * 12 é a quantidade de meses que ele vai pagar a casa

if prestacao_mensal <= (salario * 0.3):
    print('Empréstimo aprovado!')
else:
    print('Empréstimo negado!')