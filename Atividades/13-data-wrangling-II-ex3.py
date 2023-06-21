# Módulo | Análise de dados: Data Wrangling II

'''
3. Brasil

Utilize o pacote Python pandas para combinar os dados do arquivo estados-limpo.csv com os dados do arquivo cidades-limpo. csv em um único dataframe. Escolha a coluna e o método de combinação de tal forma que não haja perda de dados no processo (não produzirá valores nulos NaN ). Salve os dados do dataframe no arquivo brasil.csv
'''

import pandas as pd

# Lê o arquivo CSV dos estados
estados = pd.read_csv('./arquivos/13/estados-limpo.csv', sep=';')

# Lê o arquivo CSV das cidades
cidades = pd.read_csv('./arquivos/13/cidades-limpo.csv', sep=';', encoding='latin_1', index_col=[0])

# Combina os dados das cidades e dos estados usando a coluna 'estado' em comum
dados = cidades.merge(estados, on='estado', how='left')

# Salva os dados combinados em um novo arquivo CSV
dados.to_csv('./arquivos/13/brasil.csv', sep=';', encoding='latin_1')

# Sucesso
print('Arquivo CSV gerado com sucesso!')
