# Módulo | Análise de dados: Fundamentos de Matemática

# 2. NumPy - Quantidade de incidentes por dia

import numpy as np

data = None

# Lê o arquivo CSV com os dados de incidentes de trânsito
with open(file='./arquivos/16/traffic.csv', mode='r', encoding='utf8') as fp:
    fp.readline()
    # Armazena os dados lidos do arquivo como uma string
    data = fp.read()

dia = 14
incidentes = 0
# Cria um dicionário para armazenar o total de incidentes por dia
incidentes_por_dia = dict()

for intervalo_tempo in data.split(sep='\n'):
    # Separa os dados do intervalo de tempo em caixas de tempo individuais
    dados_intervalo = intervalo_tempo.split(sep=';')

    # Converte as contagens de incidentes para uma matriz NumPy
    array_incidentes = np.array([int(i) for i in dados_intervalo[1:-1]])
    # Soma o total de incidentes no intervalo de tempo atual
    incidentes = incidentes + np.sum(array_incidentes)

    try:
        # Obtém o valor da meia hora do intervalo de tempo
        meia_hora = int(dados_intervalo[0])

        # Verifica se é a meia hora correspondente
        if meia_hora == 27:
            # Armazena o total de incidentes para o dia atual no dicionário
            incidentes_por_dia[dia] = incidentes
            # Atualiza para o próximo dia e reinicia a contagem de incidentes
            dia = dia + 1
            incidentes = 0
    except ValueError:
        # Ignora o intervalo de tempo se ocorrer um erro
        continue

for dia in incidentes_por_dia:
    # Imprime o total de incidentes para cada dia
    print(f'Dia {dia}: Total de incidentes = {incidentes_por_dia[dia]}')
