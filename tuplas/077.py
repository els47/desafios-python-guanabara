# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais

palavras = ('banana', 'palmeiras', 'botafogo', 'esportes', 'risada')

for p in palavras: # Percorre todas as palavras da lista
    print(f'\n Na palavra {p.upper()} temos ', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou': # Percorre as letras de cada palavra
            print(letra, end=' ')