import pandas as pd
from teste_2 import dataset


nomes = dataset['Nome']
valor = dataset['Valor']

lista = dict(zip(nomes, valor))

#dict #key // mostra elemento na dict
print(lista['Palio Weekend'])

#dict #key // consulta se um elemento pertence ou nao em uma dict
print('Palio Weekend' in lista)

#del #dict #key // deleta elemento da dict
del lista['Palio Weekend']

#func #dict // mostra o total de itens da dict
print(len(lista))



