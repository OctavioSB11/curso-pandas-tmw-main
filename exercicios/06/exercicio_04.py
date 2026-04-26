# %%
# 06.04 - Quem teve mais transações de Streak?

import pandas as pd

# %%

transacoes = pd.read_csv("../../data/transacoes.csv", sep=";")
transacoes.head()

# %%
transacoes_produtos = pd.read_csv("../../data/transacao_produto.csv", sep=";")
transacoes_produtos.head()

# %%
produtos = pd.read_csv("../../data/produtos.csv", sep=";")
produtos.head()

# %%

cliente_transacao_produto = transacoes.merge(
    right=transacoes_produtos,
    how='left',
    on=['IdTransacao'],
    suffixes=["Transacao", "Produto"],
)

cliente_transacao_produto[['IdTransacao','IdProduto', 'IdCliente' ]]

# %%    
df_full = cliente_transacao_produto.merge(produtos, 
    how='left', 
    on=['IdProduto'], 
    suffixes=["Transacao", "Produto"]
)
df_full = df_full[df_full['DescNomeProduto'] == 'Presença Streak']
resultado = (df_full.groupby(['IdCliente'])['IdTransacao'].count()).sort_values(ascending=False)
print('Usuario com maior streak', resultado.head(1))


# %%  
# Forma mais performática de resolver o problema acima

# Filtrar os produtos antes de fazer o merge
produtos = produtos[produtos["DescNomeProduto"]=="Presença Streak"]

# Fazer o merge e contar as transações
(transacoes.merge(transacoes_produtos, on=["IdTransacao"], how="left") 
            # Parte das transações que contém streak
           .merge(produtos, on=["IdProduto"], how="inner")
            # Agrupa por cliente e conta as transações
           .groupby(by=["IdCliente"])["IdTransacao"]
           .count()
            # Ordena e pega o maior
           .sort_values(ascending=False)
           .head(1)
)