# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. As cédulas disponíveis serão as de R$50, R$20, R$10 e R$1. Observe que o programa não deve se preocupar com a quantidade de cédulas disponíveis na máquina.
# OBS: Considere que o caixa possui cédulas limitadas a R$50, R$20, R$10 e R$1


v = int(input('Qual valor você deseja sacar? '))
total = v
ced = 50
tot_ced = 0
while True:
    if total >= ced:
        total -= ced  # Retira o máximo de cédulas presentes no valor
        tot_ced += 1  # Contabiliza a quantidade de cédulas retiradas
    else:
        if tot_ced > 0:  # Se as cédular não forem retiradas, a quantidade zerada não é exibida
            print(f'Total de {tot_ced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced ==10:
            ced = 1
        tot_ced = 0
        if total == 0:
            break 
print('Sistema finalizado!')