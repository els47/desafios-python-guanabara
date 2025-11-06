# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Digite o sexo [M/F]:')).upper().strip()[0] 
while sexo not in 'MF':
    sexo = str(input('Digite o sexo [M/F]:')).upper().strip()[0] # Retira os espaços do início e do final, pega a primeira letra e transforma em maiúscula
print(f'O sexo digitado foi {sexo}')