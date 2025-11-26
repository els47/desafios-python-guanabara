# Crie um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista

lista = [ ]
maior = menor = 0

for contador in range(5):
    n = int(input("Digite um número: "))
    lista.append(n)

    if contador == 0:
        maior = menor = lista[contador]
    else:
        if lista[contador] > maior:
            maior = lista[contador]
        if lista[contador] < menor:
            menor = lista[contador]

print(f'Esta é a lista com os números digitados: {lista}')

for i, v in enumerate(lista):
    if v == maior:
        print(f'O maior número digitado foi {max(lista)}, que está na {i + 1}ª posição')

for i, v in enumerate(lista):
    if v == menor:
        print(f'O menor número digitado foi {min(lista)}, que está na {i + 1}ª posição')