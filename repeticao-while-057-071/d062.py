# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro_termo = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
termo = primeiro_termo
cont = 1
total = 0
mais = 10 # É a quantidade inicial já demonstrada na PA

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f"{termo} - ", end='')
        termo += razao
        cont += 1
    print("Pausa")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print("Fim")