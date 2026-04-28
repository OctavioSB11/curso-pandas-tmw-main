# %%
# 06.05 - Qual a média de transações / dia?

import pandas as pd

df = pd.read_csv("../../data/transacoes.csv", sep=';')
df

#%%

df['dtDia'] = pd.to_datetime(df['DtCriacao']).dt.date

# %%

summary = df.agg({
    "IdTransacao": 'count',
    "dtDia": 'nunique',
})

transacoe_dia = summary["IdTransacao"] / summary["dtDia"]
transacoe_dia