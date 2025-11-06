# Cria um programa que leia dois valores e mostre um menu na tela:

# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso.

# Recebendo os dois valores

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))


# Exibindo o menu e recebendo a opção do usuário
opcao = 0
while opcao !=5:
    print('Digite a opção desejada:'
    '[ 1 ] somar '
    '[ 2 ] multiplicar '
    '[ 3 ] maior '
    '[ 4 ] novos números '
    '[ 5 ] sair do programa')
    opcao = int(input('Sua opção: '))
    if opcao == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}')
    elif opcao == 2:
        print(f'O resultado da multiplicação entre {n1} e {n2} é {n1 * n2}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior valor entre {n1} e {n2} é {maior}')
    elif opcao == 4:
        print('Informe os números novamente.')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Saindo do programa...')
    else:
        print('Opção inválida. Tente novamente!')
print('Programa encerrado!')
    