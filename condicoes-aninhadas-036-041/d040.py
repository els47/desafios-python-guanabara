# Crie um programa que leia duas notas de um aluno e calcule uma mensagem no final, de acordo com a média atingida: média abaixo de 5 reprovado; entre 5 e 6.9 recuperação; igual ou maior que 7 será aprovado

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

if n1 + n2 / 2 < 5:
    print('REPROVADO')
elif 5 <= n1 + n2 / 2 < 7:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')