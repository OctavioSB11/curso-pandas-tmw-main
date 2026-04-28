# %%
# 06.03 - Qual usuário teve maior quantidade de pontos debitados?

import pandas as pd

df = pd.read_csv("../../data/transacoes.csv", sep=';')
df

# %%

filtro = df['QtdePontos'] < 0

(df[filtro].groupby(by='IdCliente')['QtdePontos']
                   .sum()
                   .sort_values(ascending=True)
                   .head(1))