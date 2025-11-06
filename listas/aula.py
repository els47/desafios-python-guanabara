valores = []

for v in range (20):
    valor = int(input('Digite um valor: '))
    valores.append(valor)

maior = max(valores)
menor = min(valores)

print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')


