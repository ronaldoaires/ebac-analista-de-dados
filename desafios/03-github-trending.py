'''
Desafio:

Utilize os pacotes Python requests e BeautifulSoup para extrair os 10 projetos mais populares do GitHub. Acesse o link https://github.com/trending

Escreva os dados extraídos no arquivo csv github.csv separado por ;
'''

import requests
import csv
from bs4 import BeautifulSoup as soup
from requests.exceptions import HTTPError

conteudo = None

try:
    # Faz a requisição HTTP para a página
    resposta = requests.get('https://github.com/trending')
    resposta.raise_for_status()
except HTTPError as exc:
    print(exc)
else:
    # Obtém o conteúdo da resposta
    conteudo = resposta.text

# Faz o parsing do conteúdo HTML utilizando a biblioteca BeautifulSoup
pagina = soup(conteudo, 'html.parser')

# Obtendo os repositórios
repositorios = pagina.find_all("article", class_="Box-row")

# Abre o arquivo CSV no modo de append
with open(file='./arquivos/github.csv', mode='a', newline='', encoding='utf8') as arquivo:
    # Cria um objeto writer do módulo csv
    escrever = csv.writer(arquivo, delimiter=';')

    # Escreve o cabeçalho
    escrever.writerow(['ranking', 'project', 'language',
                      'stars', 'stars_today', 'forks'])

    # Iterando pelos repositórios e extraindo informações
    for i, repositorio in enumerate(repositorios[:10], start=1):
        # Obtendo o título
        titulo = repositorio.find("h2")
        # Separando o título em usuário e repositório
        titulo = titulo.text.strip().replace("\n", "").replace(" ", "").split("/")
        usuario = titulo[0]
        projeto = titulo[1]

        # Obtendo a linguagem
        linguagens_tag = repositorio.find(
            "span", itemprop="programmingLanguage")
        if linguagens_tag:
            linguagem = linguagens_tag.text.strip()

        # Obtendo o número de estrelas
        estrelas_tag = repositorio.find(
            "a", class_="Link--muted d-inline-block mr-3")
        if estrelas_tag:
            estrelas = estrelas_tag.text.strip()

        # Obtendo o total de forks
        forks_tag = repositorio.find("a", href=f"/{usuario}/{projeto}/forks")
        if forks_tag:
            forks = forks_tag.text.strip()

        # Obtendo o total de estelas do dia
        estrelas_hoje_tag = repositorio.find(
            "span", class_="d-inline-block float-sm-right")
        if estrelas_hoje_tag:
            estrelas_hoje = estrelas_hoje_tag.text.strip().replace(" ",
                                                                   "/").split("/")[0]

        # Escreve os dados no arquivo CSV
        escrever.writerow(
            [i, projeto, linguagem, estrelas, estrelas_hoje, forks])

# Mensagem de sucesso
print('Trending CSV gerado com sucesso!')
