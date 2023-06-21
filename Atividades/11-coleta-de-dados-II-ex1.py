# Módulo | Análise de dados: Coleta de Dados II

# 1. Arquivo Robots.txt - Utilize o pacote Python requests para fazer o download do conteúdo do arquivo robots.txt do site do IMDB e salve numa variável chamada robots. Com o conteúdo na variável robots , verifique se a palavra top ou charts está presente no conteúdo do texto. Se sim, imprima True , senão imprima False.

import requests
from requests.exceptions import HTTPError

def crawl_website(url: str) -> str:
    try:
        # Faz a requisição GET para o URL especificado
        resposta = requests.get(url)
        
        # Verifica se ocorreu um erro na requisição
        resposta.raise_for_status()
    except HTTPError as exc:
        # Se ocorrer um erro HTTP, exibe a mensagem de erro
        print(exc)
    else:
        # Se a requisição for bem-sucedida, retorna o conteúdo da resposta
        return resposta.text

# URL do arquivo robots.txt do IMDb
url = 'https://www.imdb.com/robots.txt'

# Faz o crawling do website e obtém o conteúdo do arquivo robots.txt
robots = crawl_website(url)

# Verifica se as palavras 'top' ou 'charts' estão presentes no conteúdo do arquivo
if 'top' in robots or 'charts' in robots:
    print(True)
else:
    print(False)
