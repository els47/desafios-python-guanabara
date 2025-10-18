# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1.250.00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%

# Recebendo o salário de um funcionário

salario = int(input('Digite o seu salário:'))

# Calculando o reajuste

if salario > 1250:
    print(f'Seu novo salário é {salario * 1.10}')
else:
    print(f'Seu novo salário é {salario * 1.15}')