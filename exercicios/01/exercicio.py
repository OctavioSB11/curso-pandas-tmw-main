
# %%
import pandas as pd
# Leia o arquivo transacoes.csv com a formatação correta;
# Adicione uma coluna com valores 1;
# Salve o dataframe com nome: transacoes_1.csv
transacoes = pd.read_csv("../../data/transacoes.csv", sep=";")
transacoes.head()

# %%

transacoes_1 = transacoes['valores_1'] = 1
transacoes_1.head()

transacoes_1.to_csv("transacoes_1.csv", index=False)