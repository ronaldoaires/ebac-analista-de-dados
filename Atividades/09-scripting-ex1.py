# Módulo | Python: Scripting

# 1. Script de Extração - Script para extrair a taxa CDI do site da B3 adaptado para ser executado 10 vezes.

import os
import time
import json
from random import random
from datetime import datetime
import requests

URL = 'https://www2.cetip.com.br/ConsultarTaxaDi/' + 'ConsultarTaxaDICetip.aspx'

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
        print("Dados não encontrado, continuando...")
        cdi = None
    except Exception as exc:
        print("Erro, parando a execução.")
        raise exc
    else:
        dado = json.loads(response.text)
        cdi = float(
            dado['taxa'].replace(',', '.')
        ) + (random() - 0.5)

    # Verificando se o arquivo existe
    if os.path.exists(arquivo) == False:
        with open(file=arquivo, mode='w', encoding='utf8') as fp:
            fp.write('data,hora,taxa\n')

    # Salvando dados no arquivo
    with open(file=arquivo, mode='a', encoding='utf8') as fp:
        fp.write(f'{data},{hora},{cdi}\n')
        time.sleep(2 + (random() - 0.5))

print("Sucesso!")
