# %%

import pandas as pd
import numpy as np

transacoes = pd.read_csv("../data/transacoes.csv", sep=';')
transacoes.head()

# %%

# Calcular amplitude e calcular distância da amplitude pra media, elevar ao quadrdado e fazer raiz quadrada

def diff_amp(num: pd.Series):
    amplitude = num.max() - num.min()
    media = num.mean()
    return np.sqrt((amplitude-media)**2)

# %%
# Calcular tempo de atividade do usuario

def life_time(x: pd.Series):
    dt = pd.to_datetime(x)
    return (dt.max() - dt.min()).days

# %%
summary = (transacoes.groupby(by=["IdCliente"], as_index=False)
           .agg({
               "IdTransacao": ['count'],
               "QtdePontos": ["sum", "mean", diff_amp],
               "DtCriacao": [life_time]
           }) 
)
summary.columns = [
    'IdCliente', 
    'qtdeTransacao', 
    "totalPontos", 
    "mediaPontos", 
    "ampMeanDiff", 
    "lifeTime"
]
summary