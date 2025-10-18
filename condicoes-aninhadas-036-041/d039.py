# Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade
# # Se ele ainda vai se alistar ao serviço militar
# # Se é a hora de se alistar
# # Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = atual - ano

if idade < 18:
    print(f'Ainda faltam {18 - idade} anos para o alistamento')
elif idade == 18:
    print('É a hora de se alistar!')
else:
    print(f'Já passou do tempo de alistamento, você deveria ter feito há {idade - 18} ano(s)')

