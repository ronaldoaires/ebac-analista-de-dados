# Módulo | Análise de dados: Fundamentos de Estatística

# 2. Métricas

# Para cada array você deve calcular as seguintes métricas: média e desvio padrão.

import numpy as np
import pandas as pd

dados_df = pd.read_csv('./arquivos/16/traffic.csv', sep=';')
dados_df.head()

# Declaração de variáveis
day = 14
incidents = 0

# Inicialização de dicionário e lista para armazenar os incidentes por dia
incidents_by_day = {}
incident_list = []

# Criação do dicionário de arrays de incidentes por dia
for _, row in dados_df.iterrows():
    # Calcula o total de incidentes para cada intervalo de tempo
    incidents += np.sum(row.iloc[1:-1])

    # Adiciona o total de incidentes à lista para o dia atual
    incident_list.append(incidents)

    # Reinicia o contador de incidentes para o próximo intervalo de tempo
    incidents = 0

    # Verifica se é a 14ª meia hora do dia
    if row[0] == 27:
        # Armazena o array de incidentes para o dia atual no dicionário
        incidents_by_day[day] = np.array(incident_list)

        # Atualiza o dia para o próximo
        day += 1

        # Reinicia a lista de incidentes para o próximo dia
        incident_list = []

for day, value in incidents_by_day.items():
    # Total de incidentes
    incidentes = np.sum(value)
    # Média
    media = np.mean(value)
    # Desvio padrão
    desvio = np.std(value)

    # Imprime as métricas formatadas
    print(f'Dia {day}, teve {incidentes} incidentes, uma média de {media:.2f} e desvio padrão de {desvio:.2f}')


# 3. Interpretação

# Qual dia apresenta a maior média de acidentes por meia hora?
# R: Dia 16, teve 94 incidentes, uma média de 3.48 e desvio padrão de 3.05

# Qual dia apresenta a menor variação de acidentes por meia hora?
# R: Dia 14, teve 16 incidentes, uma média de 0.59 e desvio padrão de 1.19


