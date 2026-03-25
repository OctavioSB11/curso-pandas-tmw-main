# %%
import pandas as pd

# %%
# 04.01 - Quantos clientes tem vínculo com a Twitch?

clientes = pd.read_csv("../../data/clientes.csv", sep=';')
clientes.head()

filtro_clientes_twitch = clientes["flTwitch"] == 1
qtde_twitch = clientes[filtro_clientes_twitch].shape[0]
print(f"Temos {qtde_twitch} usuários com twitch")

# %%
# 04.02 - Quantos clientes tem um saldo de pontos maior que 1000?

clientes.head()
filtro_clientes_mais_1000 = clientes["qtdePontos"] > 1000
qtde_mais_1000_pts = clientes[filtro_clientes_mais_1000].shape[0]
print(f"Temos {qtde_mais_1000_pts} usuários com mais de 1000 pontos")

# %%
# 04.03 - Quantas transações ocorreram no dia 2025-02-01?

transacoes = pd.read_csv("../../data/transacoes.csv", sep=';')
transacoes.head()


filtro = (transacoes['DtCriacao'] >= '2025-02-01') & (transacoes['DtCriacao'] < '2025-02-02')
qtd_transacoes = transacoes[filtro].shape[0]
print(f"No dia 2025-02-01 tivemos {qtd_transacoes} transações")