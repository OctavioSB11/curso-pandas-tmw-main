# %%

import pandas as pd

# %%

df = pd.DataFrame({
    "nome": ['teo', 'lara', 'nah', 'bia', 'mah', 'lara', 'mah', 'mah'],
    "sobrenome": ['calvo', 'calvo', 'ataide', 'ataide', 'silva', 'silva', 'silva', 'silva'],
    "salario": [2132, 1231, 454, 6543, 6532, 4322, 987, 2134],
})

df
# %%
# Ordeno a coluna salario e removo os duplicados diretamente
df = df.sort_values("salario", ascending=False).drop_duplicates(subset=["nome", "sobrenome"])


# %%

# Obtenha a última linha de transacao de cada cliente
# Obtenha a primeira

import pandas as pd

df = pd.read_csv("../../data/transacoes.csv", sep=';')
df.head()

# %%
# ultima
ultima_transacao = (df.sort_values(by="DtCriacao")
                      .drop_duplicates(subset=['IdCliente'], keep='last'))

# %%
primeira_transacao = (df.sort_values(by="DtCriacao")
                        .drop_duplicates(subset=['IdCliente'], keep='first'))