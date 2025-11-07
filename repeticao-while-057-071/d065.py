# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

r = 'S'
soma = quantidade = media = maior = menor = 0

while r in 'Ss':
    num = int(input("Digite um número: "))
    soma += num
    quantidade += 1 # Assume o papel do contador
    if quantidade == 1:
        maior = menor = num # Se só tiver um valor, ele será o maior e menor porque não pode ser comparado
    else:
        if num > maior: # Se o novo número for MAIOR do que o anterior:
            maior = num # A variável 'maior' receberá esse novo número ao invés do anterior, que será considerado menor
        if num < menor: # Se o novo número for MENOR do que o anterior:
            menor = num  # A variável 'menor' receberá esse novo número ao invés do anterior, que será considerado maior
    r = str(input("Quer continuar? [S/N]: ")).upper().strip()[0] # Considerar maiúsculo, minúsculo, retirar os espaços e a primeira letra digitada
media = soma / quantidade
print(f"Você digitou {quantidade} números e a média foi {media}")
print(f"O maior valor foi {maior} e o menor {menor}")