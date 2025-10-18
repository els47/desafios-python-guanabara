# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário; 2 para octal; 3 para hexadecimal

# Recebendo um número inteiro
n = int(input('Digite um número inteiro: '))

# Criando um menu de opções
print('Escolha a base de conversão: 1 para binário; 2 para octal; 3 para hexadecimal')

# Recebendo a opção do usuário
base = int(input('Sua opção:'))

# Realizando as conversões

if base == 1:
    print(f'{n} convertido para binário é igual a {bin(n)}')
elif base == 2:
    print(f'{n} convertido para octal é igual a {oct(n)}')
else:
    print(f'{n} convertido para hexadecimal é igual a {hex(n)}')
