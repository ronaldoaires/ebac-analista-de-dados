# Módulo | Análise de dados: Data Wrangling II

'''
2. Cidades

O arquivo cidades-bruto.csv contém informações demográficas e socioeconomicas das cidades do Brasil. Utilize o pacote Python pandas para extrair os dados do arquivo cidades-bruto.xml seguindo as especificações:

Apenas dados do censo de 2010;
Apenas as colunas UF, Nome, PIB, Pop_est_2009 e PIB_percapita.

Salve os dados extraídos no arquivo cidades-limpo.csv separado por ;
'''

import pandas as pd

# Lê o arquivo CSV usando o pandas
dados = pd.read_csv('./arquivos/13/cidades-bruto.csv', sep=',')

# Seleciona as colunas desejadas
dados = dados[['UF', 'nome', 'PIB', 'Pop_est_2009', 'PIB_percapita', 'Censo']]

# Filtra os dados para considerar apenas o Censo de 2010
dados = dados.query('Censo == 2010')

# Remove a coluna 'Censo'
dados = dados.drop(['Censo'], axis=1)

# Renomeia as colunas
dados = dados.rename(columns={'UF': 'estado', 'nome': 'cidade', 'PIB': 'pib', 'Pop_est_2009': 'populacao',
                              'PIB_percapita': 'pib_percapita'})

# Salva os dados em um novo arquivo CSV
dados.to_csv('./arquivos/13/cidades-limpo.csv', sep=';', encoding='latin_1')

# Mensagem de sucesso
print('Arquivo CSV gerado com sucesso!')
