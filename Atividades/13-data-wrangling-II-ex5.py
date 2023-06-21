# Módulo | Análise de dados: Data Wrangling II

# 4. Visualização - Utilize o dataframe brasil_df para gerar as seguintes visualizações de cada item

import pandas as pd

# Lendo arquivo CSV
brasil_df = pd.read_csv('./arquivos/13/brasil.csv', sep=';', encoding='latin_1') 

# Gráfico de barras com as 10 cidades menos populosas
menor_populacao = brasil_df.groupby('cidade').sum()
menor_populacao = brasil_df.sort_values('populacao')
menor_populacao = menor_populacao[['cidade','populacao']]

menor_populacao[:10].plot(y='populacao', x='cidade', kind='bar', figsize=(10,5))

# Gráfico de pizza com a proporção da população do Brasil por região.
brasil_regiao = brasil_df.groupby('regiao').sum()
brasil_populacao = brasil_regiao[['populacao']]

brasil_populacao.plot.pie(y='populacao', figsize=(10,10))
