# %%
# 05.05 - Selecione a primeira transação diária de cada cliente.
import pandas as pd

transacoes = pd.read_csv("../../data/transacoes.csv", sep=";")
transacoes.head()
# %%
#Ordenamos a coluna
transacoes = transacoes.sort_values("DtCriacao", ascending=False)
#Passamos a data para date time e usamos o dt.date 
transacoes["data"] = pd.to_datetime(transacoes["DtCriacao"]).dt.date
#Removemos as duplicatas manntendo o primeiro IdCliente e a primeira data de criação por estar ordenada
transacoes.drop_duplicates(keep="first", subset=["IdCliente", "DtCriacao"])

# %%
# 05.05 - Selecione a primeira transação diária de cada cliente.

import pandas as pd

transacoes = pd.read_csv("../../data/transacoes.csv", sep=';')
transacoes.head()

transacoes["data"] = pd.to_datetime(transacoes["DtCriacao"]).dt.date
transacoes = transacoes.sort_values("DtCriacao")

# %%

first = transacoes.drop_duplicates(keep="first", subset=["IdCliente", "data"])
last = transacoes.drop_duplicates(keep="last", subset=["IdCliente", "data"])

pd.concat([last, first])