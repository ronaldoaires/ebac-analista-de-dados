# Módulo | Análise de Dados: Visualização Interativa de Dados

'''
1. Contexto

Você é o analista de dados de um grande aeroporto. O time de operações precisa acompanhar o fluxo mensal de passageiros para tomar decisões sobre manutenção, obras, etc. Você propõe a construção de um *dashboard* de dados para auxiliar o time na tomada de decisão.
'''

# 2. Preparação

# Bibliotecas
import seaborn as sns

# 2.1. Extração

# Carrega os dados de voos (flights)
voos = sns.load_dataset('flights')

'''
Responda:

Qual é a granularidade temporal da base de dados: 
R: Mensal

Qual é o intervalo de tempo (min/max): 
voos.head()
voos.tail()
R: Janeiro de 1949 a Dezembro de 1960
'''

# 2.2. Transformação

# Tranforme o texto da coluna month para sua representação numérica, exemplo: Jan para 1 e Dec para 12.

# Dicionário de correspondência entre meses e números
meses = {
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4,
    'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8,
    'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
}
# Substitui os valores usando replace
voos['month'] = voos['month'].replace(meses)

# Cria uma chave temporal year-month no formato YYYY-MM através da concatenação das colunas year e month, exemplo: 1949-01.
voos['year_month'] = voos['year'].astype(str) + '-' + voos['month'].astype(str).astype(str).str.zfill(2)

# Reordena as colunas da seguinte forma: year-month, year, month e passengers.
voos = voos[['year_month','year','month','passengers']]

# Salva o DataFrame em um arquivo com o nome flights.csv, no formato CSV
voos.to_csv('./arquivos/23/flights.csv', sep=',', index=False)