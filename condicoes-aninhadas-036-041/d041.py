# A CFN precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: até 9 anos é mirim; até 14 anos é infantil; até 19 anos é junior; até 25 anos é sênior; acima é master

ano = int(input('Ano de nascimento: '))
idade = 2025 - ano

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')