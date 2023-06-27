# Módulo | Análise de dados: Fundamentos de Estatística

# 1. Agregação

# Gere um array NumPy por dia. Para cada array você deve somar todos os incidentes que aconteceram naquela meia hora. Sendo assim, cada array deve ter 27 posições, cada qual com a soma dos incidentes daquela meira hora.

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

# Imprime o dicionário de arrays de incidentes por dia
for day, value in incidents_by_day.items():
    print(f'{day}: {value}')

