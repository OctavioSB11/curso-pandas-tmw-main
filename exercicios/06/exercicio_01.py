# 06.01 - Qual a quantidade média de redes sociais dos usuários? E a Variância? E o máximo?
#%%
import pandas as pd

clientes = pd.read_csv("../../data/clientes.csv", sep=';')
clientes


redes = ['flEmail', 'flTwitch', 'flYouTube', 'flBlueSky', 'flInstagram']

clientes[redes].sum(axis=1).describe()
