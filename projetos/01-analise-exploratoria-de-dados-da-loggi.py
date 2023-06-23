# Análise Exploratória de Dados de Logística da Loggi

'''
1. CONTEXTO

A seguinte análise de dados tem como objetivo investigar as questões de logística enfrentadas pelos hubs regionais da Loggi. O foco é entender como essas questões afetam a eficiência das entregas e encontrar maneiras de melhorá-las. Ao explorar esses dados, esperamos obter insights sobre as rotas de entrega atuais e sugerir soluções para torná-las mais eficientes e ágeis.
'''

# 2. PACOTES E BIBLIOTECAS

import json
import geopandas
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim


# 3. EXPLORAÇÃO DE DADOS

# Tenta abrir o arquivo JSON
try:
    with open('./arquivos/01/deliveries.json', mode='r', encoding='utf8') as arquivo:
        dados = json.load(arquivo)
# Captura a exceção se o arquivo não for encontrado
except FileNotFoundError:
    print("O arquivo não foi encontrado.")

# Cria um DataFrame com os dados do arquivo JSON
entregas_df = pd.DataFrame(dados)

# Exibe as primeiras linhas do DataFrame
display(entregas_df.head())

'''
Os dados coletados revelam que as colunas origin e deliveries estão armazenando os dados no formato JSON. Para obter resultados precisos e confiáveis, é fundamental realizar a coleta e o pré-processamento dos dados com cuidado. Portanto, é necessário normalizar os dados, separando-os em novas colunas para facilitar a análise.
'''

# Normaliza a coluna 'origin' do DataFrame entregas_df
hub_origem_df = pd.json_normalize(entregas_df['origin'])

# Junta os DataFrames entregas_df e hub_origem_df com base nos índices
entregas_df = pd.merge(left=entregas_df, right=hub_origem_df, how='inner', left_index=True, right_index=True)

# Remove a coluna 'origin' do DataFrame entregas_df
entregas_df = entregas_df.drop('origin', axis=1)

# Organiza as colunas do DataFrame entregas_df na ordem desejada
colunas = ['name', 'region', 'lng', 'lat', 'vehicle_capacity', 'deliveries']
entregas_df = entregas_df[colunas]

# Renomeia as colunas do DataFrame entregas_df
entregas_df = entregas_df.rename(columns={
    'name': 'nome',
    'region': 'regiao',
    'lng': 'hub_longitude',
    'lat': 'hub_latitude',
    'vehicle_capacity': 'capacidade',
    'deliveries': 'entregas'
})

# Exibe as primeiras linhas do DataFrame entregas_df
display(entregas_df.head())


'''
Inicialmente, normalizamos a coluna "origin", convertendo as informações JSON em novas colunas. Em seguida, adicionamos estas colunas ao nosso dataframe e removemos a coluna "origin". Para fins didáticos e para tornar o processo mais compreensível, também renomeamos todas as colunas.
'''

# Cria um novo DataFrame onde cada linha representa uma entrega individual
entregas_explode_df = entregas_df[['entregas']].explode('entregas')

# Exibe as primeiras linhas do DataFrame entregas_explode_df
display(entregas_explode_df.head())

'''
A coluna "entregas" apresenta uma lista de informações aninhadas no formato JSON. Para lidar com esses dados aninhados, vamos normalizá-los com uma operação chamada "explode", que irá transformar cada item da lista em uma linha individual. Por fim, faremos o "flatten" do resultado, simplificando a estrutura da coluna.
'''

# Normaliza as colunas "size", "point.lng" e "point.lat" do DataFrame entregas_explode_df
entregas_normalizada_df = pd.concat([
    pd.DataFrame(entregas_explode_df["entregas"].apply(lambda record: record["size"])).rename(columns={"entregas": "entrega_tamanho"}),
    pd.DataFrame(entregas_explode_df["entregas"].apply(lambda record: record["point"]["lng"])).rename(columns={"entregas": "entrega_longitude"}),
    pd.DataFrame(entregas_explode_df["entregas"].apply(lambda record: record["point"]["lat"])).rename(columns={"entregas": "entrega_latitude"}),
], axis=1)

# Exibe as primeiras linhas do DataFrame entregas_normalizada_df
display(entregas_normalizada_df.head())

'''
Com os dados explodidos, vamos normaliza-los para combina-los ao conjunto de dados principal. Primeiro concatenamos os DataFrames verticalmente em cada uma das linhas, aplicando o “lambda” nas colunas de interesse já renomeado as colunas. Dessa forma conseguimos extrair as colunas tamanho, longitude e latitude preservando os índices.
'''

# Exclui a coluna "entregas" do DataFrame entregas_df
entregas_df = entregas_df.drop('entregas', axis=1)

# Une os DataFrames entregas_df e entregas_normalizada_df com base nos índices
entregas_df = pd.merge(left=entregas_df, right=entregas_normalizada_df, how='right', left_index=True, right_index=True)

# Redefine os índices do DataFrame entregas_df
entregas_df.reset_index(inplace=True, drop=True)

# Exibe as primeiras linhas do DataFrame entregas_df
display(entregas_df.head())

'''
Finalmente, removemos a coluna "entregas" e combinamos os dados normalizados das entregas com o dataframe principal. Desta forma, temos os dados iniciais disponíveis para uma análise mais eficiente.
'''

# 3.1. Estrutura

entregas_df.shape
# A tabela de dados possui 636149 linhas e 8 colunas.

entregas_df.columns
# Colunas nome, regiao, latitude e longitude do hub, capacidade do veiculo, tamanho da entrega, longitude e latitude da entrega do tipo texto.

entregas_df.index
# A tabela começa do 0 até 636149 passando 1

entregas_df.info()

# O método info() exibe informações sobre o DataFrame, incluindo o número de colunas, nomes das colunas, tipos de dados, uso de memória, intervalo de índice, número de linhas em cada coluna e valores nulos. Não temos nenhum valor nulo na tabela

# 3.2. Schema

entregas_df.dtypes
# As colunas e seus respectivos tipos de dados mostram que a tabela tem dados consistentes.

entregas_df.select_dtypes("object").describe().transpose()
# Os atributos categóricos revelam que na categoria "nome", a tabela tem 636149 linhas e 199 são únicas, sendo o mais comum "cvrp-1-df-87" presente em 5636 linhas. Na categoria "regiao", com 636169 linhas, apenas 3 linhas são únicas, sendo a mais frequente "df-1", presente em 304708 linhas.

entregas_df.drop(["nome", "regiao"], axis=1).select_dtypes('int64').describe().transpose()
# Os atributos numéricos indicam que a capacidade dos veículos é uniforme em todos os centros. O tamanho das entregas varia entre 1 e 10, com bastante variação na média.

# 3.3. Dados faltantes

entregas_df.isna().any()
# Todas as colunas na tabela retornam "False" quando verificadas por valores faltantes, o que confirma que não há nenhum dado faltante na tabela.


# 4. MANIPULAÇÃO

# 4.1. Enriquecimento

'''
Geocodificação reversa do hub

A geocodificação é o processo que transforma uma localização descrita por um texto (endereço, nome do local, etc.) em sua respectiva coodernada geográfica (latitude e longitude). A geocodificação reversa faz o oposto, transforma uma coordenada geográfica de um local em suas respectivas descrições textuais.
'''

# Seleciona as colunas "regiao", "hub_longitude" e "hub_latitude" do DataFrame entregas_df
hub_df = entregas_df[["regiao", "hub_longitude", "hub_latitude"]]

# Remove duplicatas, ordena o DataFrame e redefine os índices
hub_df = hub_df.drop_duplicates().sort_values(by="regiao").reset_index(drop=True)

# Exibe as primeiras linhas do DataFrame hub_df
display(hub_df.head())

# Cria um objeto Nominatim com um nome de usuário definido
geo_app = Nominatim(user_agent="ronaldoaires")

# Obtém informações do local a partir de suas coordenadas
geo_local = geo_app.reverse("-15.838145, -48.054989")

# Exibe as informações formatadas em JSON
print(json.dumps(geo_local.raw, indent=2, ensure_ascii=False))

# Cria um objeto RateLimiter para limitar as consultas de geolocalização
geo_dados = RateLimiter(geo_app.reverse, min_delay_seconds=1)

# Cria uma nova coluna no dataframe para armazenar as coordenadas dos hubs
hub_df['coordenadas'] = hub_df['hub_latitude'].astype(str) + ',' + hub_df['hub_longitude'].astype(str)

# Cria uma nova coluna no dataframe para armazenar os dados de geolocalização
hub_df['geo_dados'] = hub_df['coordenadas'].apply(geo_dados)

# Dataframe
display(hub_df.head())

# Normaliza os dados de geolocalização e transforma em colunas
hub_geo_dados_df = pd.json_normalize(hub_df['geo_dados'].apply(lambda dados: dados.raw))

# Dataframe
display(hub_geo_dados_df.head())

# Selecionando colunas
hub_geo_dados_df = hub_geo_dados_df[["address.town", "address.suburb", "address.city"]]

# Criando colunas com base em condicionais
hub_geo_dados_df["hub_cidade"] = np.where(hub_geo_dados_df["address.city"].notna(), 
                                         hub_geo_dados_df["address.city"], 
                                         hub_geo_dados_df["address.town"])
hub_geo_dados_df["hub_bairro"] = np.where(hub_geo_dados_df["address.suburb"].notna(), 
                                         hub_geo_dados_df["address.suburb"], 
                                         hub_geo_dados_df["address.city"])

# Removendo colunas
hub_geo_dados_df.drop(["address.town", "address.suburb", "address.city"], axis=1, inplace=True)

# Dataframe resultante
display(hub_geo_dados_df.head())

# Juntando dataframes
hub_df = pd.merge(left=hub_df, right=hub_geo_dados_df, left_index=True, right_index=True)

# Selecionando colunas
hub_df = hub_df[["regiao", "hub_bairro", "hub_cidade"]]

# Dataframe  
display(hub_df.head())


# Juntando dataframes com base na coluna 'regiao'
entregas_df = pd.merge(left=entregas_df, right=hub_df, how='inner', on='regiao')

# Reorganizando as colunas do dataframe
entregas_df = entregas_df[[
    'nome',
    'regiao',
    'hub_longitude',
    'hub_latitude',
    'hub_cidade',
    'hub_bairro',
    'capacidade',
    'entrega_tamanho',
    'entrega_longitude',
    'entrega_latitude'
]]

# Exibindo as primeiras linhas do dataframe resultante
display(entregas_df.head())


# Geocodificação reversa da entrega - A geocodificação reversa é o processo de conversão de coordenadas geográficas em um endereço legível por humanos

# Lendo os dados das entregas
entregas_geo_dados_df = pd.read_csv('./arquivos/01/deliveries-geodata.csv')

# Exibindo as primeiras linhas do dataframe
display(entregas_geo_dados_df.head())


# Renomeando as colunas
entregas_geo_dados_df = entregas_geo_dados_df.rename(columns={
    'delivery_lng': 'entrega_longitude',
    'delivery_lat': 'entrega_latitude',
    'delivery_city': 'entrega_cidade',
    'delivery_suburb': 'entrega_bairro'
})

# Juntando os dataframes
entregas_df = pd.merge(left=entregas_df, right=entregas_geo_dados_df[['entrega_cidade', 'entrega_bairro']], how='inner', left_index=True, right_index=True)

# Exibindo as primeiras linhas do dataframe resultante
display(entregas_df.head())


# 4.2. Qualidade

# A qualidade dos dados está relacionado com a consistência do seu schema , valores faltantes, etc.

entregas_df.info()
# As informações da tabela mostram que ela tem 636149 índices, 12 colunas e que dessas, 2 colunas tem valores nulos sendo elas as colunas entrega_cidade e entrega_bairro

entregas_df.isna().any()
# Confirmando que as colunas entrega_cidade e entrega_bairro realmente tem valores nulos pois retornam True como resultado.

100 * (entregas_df["entrega_cidade"].isna().sum() / len(entregas_df))
# Ao analisar a coluna entrega_cidade em porcentagem, encontramos o valor de 0.26% o valor baixo indica que está dentro do esperado e está ok.

100 * (entregas_df["entrega_bairro"].isna().sum() / len(entregas_df))
# Ao analisar a coluna entrega_bairro em porcentagem, encontramos o valor de 25.13% o valor alto indica que tem uma quantidade alta de valores faltantes o que pode não ser interessante.

prop_df = entregas_df[["entrega_cidade"]].value_counts() / len(entregas_df)
prop_df.sort_values(ascending=False).head(10)

'''
Ao analisar os dados da coluna entrega_cidade em porcentagem, podemos ver um problema em relação à cidade de Brasília sendo listada, mas, na realidade, é composta por regiões. Isso pode ser um problema e pode prejudicar as análises e interpretações dos dados, especialmente se houver diferenças significativas na entrega de produtos entre essas regiões. Portanto, seria recomendável considerar a desagregação da cidade de Brasília em suas regiões correspondentes para obter uma visão mais precisa e detalhada dos dados de entrega.
'''

prop_df = entregas_df[["entrega_bairro"]].value_counts() / len(entregas_df)
prop_df.sort_values(ascending=False).head(10)

'''
Ao analisar os dados da coluna entrega_bairro em porcentagem, podemos ver que, assim como na coluna entrega_cidade, existem registros de bairros inexistentes, como o bairro de Brasília. Embora esses registros possam representar apenas uma pequena porcentagem do total de entregas, eles ainda podem ser um problema e prejudicar as análises e interpretações dos dados. Se houver diferenças significativas nas entregas para esses bairros inexistentes em comparação com os bairros reais, isso pode distorcer a imagem geral dos resultados e levar a conclusões equivocadas.
'''

# 5. VISUALIZAÇÃO

# 5.1. Mapa de entregas por região
# 5.1.1 Mapa do Distrito Federal

# Lendo o arquivo shapefile do Distrito Federal
mapa = geopandas.read_file("./arquivos/01/LIM_Unidade_Federacao_A.shp")

# Selecionando apenas a primeira linha do shapefile
mapa = mapa.loc[[0]]

# Exibindo as primeiras linhas do dataframe resultante
display(mapa.head())


# 5.1.2 Mapa dos Hubs

# Selecionando as colunas desejadas, removendo duplicatas e redefinindo os índices
hub_df = entregas_df[["regiao", "hub_longitude", "hub_latitude"]].drop_duplicates().reset_index(drop=True)

# Criando um GeoDataFrame com base no DataFrame hub_df, utilizando as coordenadas como geometria
geo_hub_df = geopandas.GeoDataFrame(hub_df, geometry=geopandas.points_from_xy(hub_df["hub_longitude"], hub_df["hub_latitude"]))

# Exibindo as primeiras linhas do GeoDataFrame resultante
display(geo_hub_df.head())


# 5.1.3 Mapa das Entregas

# Criando um GeoDataFrame com base no DataFrame entregas_df, utilizando as coordenadas como geometria
geo_entregas_df = geopandas.GeoDataFrame(
    entregas_df, geometry=geopandas.points_from_xy(entregas_df["entrega_longitude"], entregas_df["entrega_latitude"])
    )

# Exibindo as primeiras linhas do GeoDataFrame resultante
display(geo_entregas_df.head())


# 5.1.4 Visualização

# Cria o plot vazio
fig, ax = plt.subplots(figsize=(50/2.54, 50/2.54))

# Plota o mapa do Distrito Federal
mapa.plot(ax=ax, alpha=0.4, color="lightgrey")

# Plota as entregas em diferentes regiões
geo_entregas_df.query("regiao == 'df-0'").plot(ax=ax, markersize=1, color="red", label="df-0")
geo_entregas_df.query("regiao == 'df-1'").plot(ax=ax, markersize=1, color="blue", label="df-1")
geo_entregas_df.query("regiao == 'df-2'").plot(ax=ax, markersize=1, color="seagreen", label="df-2")

# Plota os hubs de entrega
geo_hub_df.plot(ax=ax, markersize=30, marker="x", color="black", label="hub")

# Plota a legenda
plt.title("Entregas no Distrito Federal por Região", fontdict={"fontsize": 16})
legenda = plt.legend(prop={"size": 15})
for handle in legenda.legendHandles:
    handle.set_sizes([50])


# 5.1.5 Insights

'''
    1. As entregas estão corretamente alocadas aos seus respectivos hubs;
    2. Os hubs das regiões 0 e 2 fazem entregas em locais distantes do centro e entre si, o que pode gerar um tempo e preço de entrega maior.
'''

# 5.2. Gráfico de entregas por região

# 5.2.1 Agregação

# Calcula a proporção das entregas em cada região com base na capacidade dos hubs
dados = pd.DataFrame(entregas_df[['regiao', 'capacidade']].value_counts(normalize=True).reset_index())

# Renomeia a coluna com a proporção das entregas para 'proporcao'
dados.rename(columns={dados.columns[-1]: 'proporcao'}, inplace=True)

# Exibe as primeiras linhas do DataFrame 'dados'
display(dados.head())



# 5.2.1 Visualização

# Define o estilo do eixo como 'whitegrid'
with sns.axes_style('whitegrid'):
    # Cria o gráfico de barras utilizando o DataFrame 'dados'
    grafico = sns.barplot(data=dados, x="regiao", y="proporcao", errorbar=None, palette="pastel")
    
    # Define o título, rótulos dos eixos x e y do gráfico
    grafico.set(title='Proporção de entregas por região', xlabel='Região', ylabel='Proporção')

# 5.2.3 Insights

'''
A concentração das entregas nos hubs das regiões 1 e 2 é alta, enquanto o hub da região 0 tem uma distribuição muito baixa. No entanto, a capacidade dos veículos é a mesma para todos os hubs, o que sugere que seria possível realocar os veículos para as regiões com maior demanda de tráfego.
'''