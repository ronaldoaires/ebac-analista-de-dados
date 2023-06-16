# Módulo | Python: Scripting

# 3. Script de extração e visualização

import os
import time
import json
from random import random
from datetime import datetime
import requests
import pandas as pd
import seaborn as sns

URL = 'https://www2.cetip.com.br/ConsultarTaxaDi/ConsultarTaxaDICetip.aspx'
arquivo = './arquivos/09/taxa-cdi.csv'

# Criando a variável data e hora
for _ in range(0, 10):
    data_e_hora = datetime.now()
    data = datetime.strftime(data_e_hora, '%Y/%m/%d')
    hora = datetime.strftime(data_e_hora, '%H:%M:%S')

    # Captando a taxa CDI do site da B3
    try:
        response = requests.get(URL)
        response.raise_for_status()
    except requests.HTTPError as exc:
        print("Dados não encontrados, continuando...")
        cdi = None
    except Exception as exc:
        print("Erro, parando a execução.")
        raise exc
    else:
        dado = json.loads(response.text)
        cdi = float(dado['taxa'].replace(',', '.')) + (random() - 0.5)

    # Verificando se o arquivo existe
    if not os.path.exists(arquivo):
        with open(file=arquivo, mode='w', encoding='utf8') as fp:
            fp.write('data,hora,taxa\n')

    # Salvando dados no arquivo
    with open(file=arquivo, mode='a', encoding='utf8') as fp:
        fp.write(f'{data},{hora},{cdi}\n')
        time.sleep(2 + (random() - 0.5))

# Extraindo as colunas hora e taxa
df = pd.read_csv('./arquivos/09/taxa-cdi.csv')

# Salvando gráfico
grafico = sns.lineplot(x=df['hora'], y=df['taxa'])
_ = grafico.set_xticklabels(labels=df['hora'], rotation=90)
grafico.get_figure().savefig("./arquivos/09/cdi.png")

print("Sucesso!")
