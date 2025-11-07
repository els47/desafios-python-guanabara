# Faça um programa que leia um número inteiro qualquer e mostre o seu fatorial. Ex: 5! = 5 x 4 x 3 x 2 x 1


# Lendo o número inteiro e aplicando condições para evitar números inválidos, como negativo e decimal, que não possuem fatorial
try: # Tenta executar o que está dentro (ler e converter o número)
    numero = int(input("Digite um número inteiro ( 0 para sair ): "))
except ValueError: # Aparece se o usuário digitar algo inválido (ex: “5.5” ou “abc”)
    print("Entrada inválida! Digite apenas números inteiros.")
else: # É executado se o número não for decimal ou valor inválido
    if numero < 0:
        print(f'O {numero} é um valor negativo e, por isso, não possui fatorial!')
    elif numero == 0:
        print(f'O fatorial de {numero} é 1!')
    else:

        contador = 1 # Serve para controlar o laço
        resultado = 1 # Armazena o produto acumulado # Inicializa com um número neutro na multiplicação

        while contador <= numero: # Utiliza a variável contador por apresentar o valor que multiplicará o número do usuário
            resultado *= contador 
            contador +=  1 # O contador é incrementado após a iteração porque no próximo laço seguirá a sequência (1, 2, 3..)

        print(f'O fatorial de {numero} é {resultado}!')




