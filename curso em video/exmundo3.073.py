#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.


times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
        'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
        'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
        'São Paulo', 'Fluminense', 'Sport Recife',
        'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
        'Atlético-GO')
for t in  times:
    print(t)
print('-=' * 20)
print(f'Os 5 primeiros times sâo: {times[:5]}')
print('-=' *20)
print(f'Os 4 últimos colocados são: {times[-4:]}')
print('-=' * 20)
print('Times em ordem alfabética:')
for time in sorted(times):
    print(time)
print('-=' * 20)
print(f'O Time Chapecoense está na {times.index("Chapecoense")+1}ª posição.')
print('-=' * 20)
