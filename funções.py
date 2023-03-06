#funções de construção

# https://docs.python.org/3.6/library/functions.html

#Pandas

import pandas as pd

dataset = pd.read_csv(r'C:\Users\guife\Desktop\workspace\curso\data\db.csv', sep = ';')

dt = dataset.get(['Nome', 'Quilometragem'])

(zip(tuple(dt)))


dt = pd.DataFrame(dt)

dt = dt[['Quilometragem', 'Nome']]

print(dt)


