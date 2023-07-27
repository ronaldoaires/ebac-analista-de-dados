# Módulo | Análise de Dados: Aprendizado de Máquina, Agrupamento

'''
1. Conjunto de dados Iris

Neste código, vamos realizar uma análise exploratória de um conjunto de dados chamado "Iris", que contém informações sobre diferentes espécies de flores do gênero Iris. O objetivo é agrupar as flores com base em suas características físicas (variáveis preditivas).
'''

# Importando as bibliotecas
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans

# Carregando os dados
dados = sns.load_dataset('iris')

# Removendo a coluna "species" que não será usada na análise
dados = dados.drop(['species'], axis=1)

# 1.1. Analise exploratória

# Utilize os gráficos abaixo para entender melhor a relação entre os atributos da base de dados.

# Atributos preditivos
with sns.axes_style('whitegrid'):
  grafico = sns.pairplot(data=dados)

# Comentário: É possível observar especialmente nas medidas das pétalas, que o conjunto de dados tem presença de dois grupos distintos.

# 2. Dados

# 2.1. Valores nulos - Checa se a base de dados possui valores faltantes.
dados.isna().sum()

# 2.2. Variáveis numéricas

# Comentário: Os dados estão na mesma escala, não tendo a necessidade de padronização.

# 2.3. Limpeza

# Comentário: Os dados estão tratados, prontos para serem usados no modelo.

# 3. Modelagem

# 3.1. Treino

# Treinando o algoritmo K-Means para agrupar as flores em diferentes grupos. O algoritmo é executado 10 vezes com diferentes números de grupos, para encontrar o número ideal de clusters
wcss = []

for k in range(1, 11):
    modelo = KMeans(n_clusters=k, n_init=k)
    modelo = modelo.fit(dados)
    wcss.append(modelo.inertia_)

# 3.2. Avaliação

# Criando um gráfico para identificar o número ideal de clusters (Método do Cotovelo)
with sns.axes_style('whitegrid'):
    grafico = sns.lineplot(
        x=range(1, 11),
        y=wcss,
        marker="8"
    )
    grafico.set(
        title='Método do Cotovelo',
        ylabel='WCSS',
        xlabel='Qtd. clusters'
    )

# Comentário: O gráfico mostra que o número ideal de clusters é 3

# 3.3. Visualização

# Treinando o algoritmo K-Means com o número ideal de clusters
modelo = KMeans(n_clusters=3, n_init='auto')
modelo = modelo.fit(dados)

# Adicionando a coluna "cluster" ao conjunto de dados
clusters = pd.concat(
    [
        dados, pd.DataFrame(modelo.labels_, columns=['cluster'])
    ],
    axis=1
)

# Gerando um gráfico para visualizar as relações entre as características físicas das flores, colorindo cada ponto de acordo com o cluster
with sns.axes_style('whitegrid'):
    graph_clusters = sns.pairplot(
        data=clusters,
        hue='cluster',
        palette="pastel"
    )

# Comentário: O gráfico mostra que o processo de clusterização resultou na separação dos dados em três conjuntos e que o cluster 0 tem características únicas.


# 4. Predição

# 4.1. Nova flor
nova_flor = np.array([5.1, 3.5, 1.4, 0.2])

# Fazendo a predição de uma nova flor com base em suas características físicas (comprimento e largura das sépalas e pétalas)
cluster = modelo.predict(nova_flor.reshape(1, -1))

# Imprimindo o resultado da predição
print(f'A nova flor seria alocada no cluster {cluster[0]}')
