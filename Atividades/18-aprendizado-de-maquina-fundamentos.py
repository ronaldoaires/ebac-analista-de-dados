# Módulo | Análise de dados: Aprendizado de máquina: Fundamentos

'''
1. Pinguins

Neste exercício, vamos utilizar uma base de dados com informações sobre penguins. A idéia é preparar a base de dados para prever a espécie do penguin (variável resposta) baseado em suas características físicas e geográficas (variáveis preditivas).
'''
import pandas as pd
import seaborn as sns

dados = sns.load_dataset('penguins')

# 1.1. Valores nulos - Trate os valores faltantes da base de dados.

dados = pd.DataFrame(dados.dropna().reset_index(drop=True))

# 1.2. Variáveis numéricas - Identifique as variáveis numéricas e crie uma nova coluna padronizando seus valores. A nova coluna deve ter o mesmo nome da coluna original acrescidade de "_std".

colunas = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']

for coluna in colunas:
    media = dados[coluna].mean()
    desvio_padrao = dados[coluna].std()
    dados[coluna + '_std'] = (dados[coluna] - media) / desvio_padrao


# 1.3. Variáveis categóricas - Identifique as variáveis categóricas nominais e ordinais, crie uma nova coluna aplicando a técnica correta de conversão a seus valores. A nova coluna deve ter o mesmo nome da coluna original acrescida de "_nom" ou "_ord".

dados['sex_m_nom'] = dados['sex'].apply(lambda sex: 1 if sex == 'Male' else 0)
dados['sex_f_nom'] = dados['sex'].apply(lambda sex: 1 if sex == 'Female' else 0)

especies = {
    'Adelie' : 0,
    'Chinstrap' : 1,
    'Gentoo' : 2
}
islands = {
    'Biscoe' : 0,
    'Dream' : 1,
    'Torgersen' : 2
}

dados['species_ord'] = dados['species'].apply(
 lambda o: especies[o]
)
dados['island_ord'] = dados['island'].apply(
 lambda o: islands[o]
)


# 1.4 Limpeza - Descarte as colunas originais e mantenha apenas a variável resposta e as variáveis preditivas com o sufixo _std", _nom" e "_ord".

dados.drop(['species', 'island','bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g','sex'], axis='columns', inplace=True)

dados.head()