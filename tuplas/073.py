# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Brasileirão, na ordem de colocação. Depois mostre
# a) Apenas os 5 primeiros colocados
# b) Os últimos 4 colocados na tabela
# c) Uma lista com os times em ordem alfabética
# d) Em que posição está o time do Cruzeiro

tabela = ('Flamengo','Palmeiras','Cruzeiro','Mirassol','Bahia','Botafogo','Fluminense','Bragantino','São Paulo','Atlético-MG', 'Vasco','Ceará', 'Corinthians','Grêmio','Internacional','Santos','Vitória','Juventude','Fortaleza','Sport')


print(f'Os 5 primeiros colocados são: {tabela[0:5]}') # No fatiamento o último número é ignorado
print(f'Os 4 últimos colocados são: {tabela[-4:]}')
print(f'A lista em ordem alfabética é: {sorted(tabela)}')
print(f'O time do Cruzeiro está na {tabela.index("Cruzeiro")+1}ª posição') # As posições iniciam no zero