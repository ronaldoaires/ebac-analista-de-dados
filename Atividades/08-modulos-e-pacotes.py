# Módulo | Python: Módulos e pacotes

# importando pacotes
import pandas as pd
import seaborn as sns

# 1. Pandas

# ler o arquivo de dados
dados_df = pd.read_csv('./arquivos/08/dow_jones_index.csv')

# Visualizando as n primeiras linhas
dados_df.head(10)

# Visualizando o nome das colunas
dados_df.columns.to_list()

# Verificando o total de linhas e colunas
linhas, colunas = dados_df.shape
print(f'Número de linhas: {linhas}')
print(f'Número de colunas: {colunas}')

# Selecionando as linha do dataframe original em que a coluna stock é igual a KO
df_cc = dados_df[dados_df['stock'] == 'KO']
df_cc.head(5)

# Selecionando apenas as colunas de data e valores de ações.
df_cc = df_cc[['date', 'open', 'high', 'low', 'close']]
df_cc.head(5)

# A função lambda remove o caracter $ e faz a conversão do tipo de str para float
for col in ['open', 'high', 'low', 'close']:
    df_cc[col] = df_cc[col].apply(
        lambda value: float(value.split(sep='$')[-1])
    )
df_cc.head(5)

# 2. Seaborn

# visualizando os valores de abertura das ações ao longo do tempo
plot = sns.lineplot(x="date", y="open", data=df_cc)
_ = plot.set_xticklabels(labels=df_cc['date'], rotation=90)

# visualizando os valores de fechamento das ações ao longo do tempo
plot = sns.lineplot(x="date", y="close", data=df_cc)
_ = plot.set_xticklabels(labels=df_cc['date'], rotation=90)

# visualizando os quatro valores no mesmo gráfico
plot = sns.lineplot(
    x="date",
    y="value",
    hue='variable',
    data=pd.melt(df_cc, ['date'])
)
_ = plot.set_xticklabels(
    labels=df_cc['date'],
    rotation=90
)

# salvando o gráfico em uma imagem png
plot.figure.savefig("./arquivos/08/cc.png")

