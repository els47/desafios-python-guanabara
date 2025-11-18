# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) Quantas pessoas têm mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres têm menos de 20 anos.

total_18 = total_h = total_m = 0

while True:
    idade = int(input('Digite a sua idade: '))
    sexo = ' ' 
    while sexo not in 'MF': # Forçar a resposta ser em Mm ou Ff
        sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
    if idade > 18:
        total_18 += 1
    if sexo == "M":
        total_h += 1
    if sexo == "F" and idade < 20:
        total_m += 1

    r = ' '
    while r not in 'SN': # Forçar a resposta ser em Mm ou Ff
        r = str(input("Cadastro realizado com sucesso! Deseja continuar? [S/N]: ")).strip().upper()[0]
    if r == 'N': # Se colocar 'Nn' não reconhece o break
        break
print('Programa finalizado!')
print(f'Foram cadastradas {total_18} pessoas maiores de 18 anos.')
print(f'Foram cadastradas {total_h} homens.')
print(f'Foram cadastradas {total_m} mulheres com menos de 20 anos.')


