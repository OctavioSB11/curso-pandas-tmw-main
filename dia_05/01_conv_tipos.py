#%% 
import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=";")


#%% 

df['qtdePontos'].astype(float)

#%% 
df['DtCriacao']

#%% 
# O replace usa um dicionario e a chave é o valor a ser mudado e o valor sera o substituto
# O replace corrige os erros de datas invalidas onde o datetime quebrava
replace = {
    "0000-00-00 00:00:00.000": "2024-02-01 09:00:00.000"
    }

df["DtCriacao"] = pd.to_datetime(
    df["DtCriacao"].replace(replace)
    ) #passa a serie 'DtCriacao' para date time e usa o replace para os casos de 0000-00-00 00:00:00.000 
df
# %%
# Após converter uma serie de datas para datetime, traz a possbilidade de usar o 'dt'
df['DtCriacao'].dt.month