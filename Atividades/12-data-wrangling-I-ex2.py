# Módulo | Análise de dados: Data Wrangling I

# 2. Data Wrangling

import pandas as pd

# Crie o dataframe Pandas na variável  fortune_df  através da leitura do arquivo  fortune.csv 
fortune_df = pd.read_csv('./arquivos/12/fortune.csv', sep=';')

# Explorando o DataFrame
# Liste as 10 primeiras linhas do dataframe:
top10 =  fortune_df.loc[0:9]

# Liste os tipos de dados armazenados na coluna do dataframe:
fortune_df.dtypes

# Liste o numero de linhas e colunas do dataframe:
linhas = fortune_df.shape[0] 
colunas = fortune_df.shape[1] 

# Limpando o DataFrame - Grande parte das colunas numéricas (exceto a coluna  ranking  e  employees ) possuem o caracter  $  ou  %  que as classificam com o tipo  object  (ou  str  do Python) ao invés do tipo correto como  int  ou  float . Utilizando os métodos de atualizar, remova os caracteres das linhas das colunas numéricas.

# Função para remover os caracteres $ e %
def remover_caracteres(valor):
    if isinstance(valor, str):
        valor = valor.replace('$', '').replace('%', '')
    return valor

# Colunas para limpar
colunas = ['revenues', 'revenues-percent-change', 'profits', 'profits-percent-change', 'assets', 'market-value']

# Usando lambda para aplicar a função
fortune_df[colunas] = fortune_df[colunas].apply(lambda x: x.apply(remover_caracteres))

# Salvando o DataFrame
fortune_df.to_csv('./arquivos/12/fortune-limpo.csv', sep=';', encoding='utf-8')

print('Arquivo CSV gerado com sucesso!')

