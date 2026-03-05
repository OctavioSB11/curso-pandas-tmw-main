# %%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")
df

# %%
df.shape

# %%
df.info(memory_usage='deep')

# %%
df.dtypes

# %%
#chave do dict -> nome antigo da coluna
#valor da chave -> novo nome da coluna
renamed_columns = {
    "qtdePontos": "qtPontos",
    "descSistemaOrigem": "SistemaOrigem"
}

# df = df.rename(columns=renamed_columns)
df.rename(columns=renamed_columns, inplace=True) #inplace -> muda diretamente o df sem precisar realocar


# %%
colunas = ["idCliente", "qtPontos"]
df[colunas]
# %%
# SELECT * FROM df
df

# %%
# SELECT idCliente FROM df

df[["idCliente"]]

# %%

# SELECT idCliente, qtPontos FROM df LIMIT 5
df[["idCliente", "qtPontos"]].tail(5)

# %%

# SELECT idCliente, idTransacao, qtPontos
# FROM df
# LIMIT 5

df[["idCliente", "idTransacao", "qtPontos"]].head(5)

# %%
# Ordenando colunas de um df, atribuimos as colunas a uma lista, usamos sort na lista e depois reatribuimos ao df
colunas = list(df.columns)
colunas.sort()
colunas

df = df[colunas]
df