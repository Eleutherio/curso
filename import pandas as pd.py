import pandas as pd

# Tuplas

nomes = tuple(['guilherme','ricardo', 'jonathan'])

# seleções em tuplas

print(nomes[-2:3])

# iterando tuplas

for nome in nomes:
    print(nome)

# desempacotamento de tuplas
# atribui uma variavel a um ou mais elementos especificos de uma tupla

nome_1, nome_2, nome_3 = nomes

print(nome_1)

_, nome_4, _ = nomes

print(nome_4)

nome_6, *_ = nomes

print(nome_6)

# zip

nomes = tuple(['guilherme','ricardo', 'jonathan'])
idades = tuple(['30','24', '22'])

list(zip(nomes, idades))

for nome, idade in zip(nomes, idades):
    print(nome, idade)

for nome, idade in zip(nomes, idades):
    if (nome != idade):
        print(nome)

